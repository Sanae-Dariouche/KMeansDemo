import pygame
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing

pygame.init()

display_width = 500
display_height = 500 

xs = []

colors = [(255, 0, 0),(0, 0, 204),(0, 204, 0),(255, 153, 0),(0,0,0),(200,0,200)]
n_clusters = int(input("Enter the number of clusters:  "))
clf = KMeans(n_clusters=n_clusters)
win = pygame.display.set_mode((display_width,display_height))
s ="KMeans Demonstration: "+str(n_clusters)+" clusters"
win.fill((209, 224, 224))
pygame.display.update()

pygame.display.set_caption(s)

clock = pygame.time.Clock()
crash = False
while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            xs.append([mouse[0],mouse[1]])
            X= np.array(xs)
            #preprocessing.scale(X)
            if len(xs)>=n_clusters:
                clf.fit(X)
                #print(X)
                labels = clf.labels_
                centroids = clf.cluster_centers_
                print(centroids)
                for i in range (len(X)):
                    pygame.draw.circle(win,colors[labels[i]],xs[i],5,5)
            else : 
                pygame.draw.circle(win,colors[0],mouse,5,5)
            pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()