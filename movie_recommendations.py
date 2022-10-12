import tkinter as ttk
import pandas as pd
import warnings

app = ttk.Tk()
app.title("Recommendation System")
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
df=pd.read_csv('u.data',sep='\t',names=cols).drop('ts',axis=1)
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',encoding='ISO-8859-1',names=item_cols)
movie=pd.merge(df,df1,on='movie_id')

result = ttk.Variable(app)

frame = ttk.Frame(app)
frame.place(x=10,y=10)


box = ttk.Listbox(frame,height=10,width =50)
for title in movie['title'].unique():
    box.insert(ttk.END , title)
box.pack(side ='left',fill = 'y')

#scroll bar 
scroll = ttk.Scrollbar(frame,orient =ttk.VERTICAL)
scroll.config(command = box.yview)
box.config(yscrollcommand = scroll.set)
scroll.pack(side ='right',fill ='y')

#movie iterate
for row,val in movie.iterrows():
    print(val['title'])
    box.insert(row+1,val['title'])

for title in movie['title'].unique():
    box.insert(ttk.END,title)
box.pack(side='left',fill='y')    
#box.place(x=10,y=10)

def get_movie():
    
       corrs=movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df=pd.DataFrame(corrs,columns={'corelation'})
    corrs_df['rating']=movie.groupby('title')['rating'].mean()
    corrs_df['count']=movie['title'].value_counts()
    
    #Find top 2-3 Recomendation
    top_recom=list(corrs_df[corrs_df['count']>50].sort_values(by='corelation',ascending=False).head(3).index)
    top_recom.remove(movie_selected)



ttk.Button(app, text="Find Recommendations", font=('Arial',22),command=get_movie).place(x=200,y=50)

ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=200,y=100)

app.mainloop()
