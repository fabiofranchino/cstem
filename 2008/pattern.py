w=1000

colors = ximport("colors")

c = colors.hex("#c1e3e0")

size(w,w)

itm=40
fill(c)
nostroke()


for x, y in grid(itm, itm, w/itm, w/itm):
    s = random(1, itm)
    fill(c)
    oval(x+w/itm/2-s/2,y+w/itm/2-s/2, s,s)