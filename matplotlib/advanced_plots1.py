import matplotlib.pyplot as plt 

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
sales  = [412,390,530,610,720,850,
          940,870,760,680,590,980]

plt.plot(months,sales)
plt.title("My Chart")

fig,ax = plt.subplots(figsize=(10,5))
ax.plot(months,sales,lw=2)
ax.set_title("My Chart",fontsize = 14)

fig = plt.figure(figsize=(12,6))
gs = fig.add_gridspec(2,3,hspace=0.4,wspace=0.3)

ax_main = fig.add_subplot(gs[:,:2])
ax_top_r = fig.add_subplot(gs[0,2])
ax_bot_r = fig.add_subplot(gs[1,2])

ax_main.plot(months,sales,color="#FF4B4B",lw=3,marker='o',mfc="white")
ax_main.set_title("Annual Sale OverView",loc = 'left',fontweight='bold')
ax_main.grid(axis='y',linestyle='--',alpha=0.7)

ax_top_r.bar(months[:3],sales[:3],color="#4B79FF")
ax_top_r.set_title("Q1 Growth")

ax_bot_r.fill_between(months[9:],sales[9:],color='#A24BFF',alpha=0.3)
ax_bot_r.plot(months[9:],sales[9:],color='#A24BFF')
ax_bot_r.set_title("Year-End Surge")

plt.show()