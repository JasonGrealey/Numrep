from scipy import misc
import matplotlib.pyplot as plt
import numpy as np 
import math

def main():
    #         Get the filename as string
    f1 = "desync1.pgm"
    #         Read file it np array
    img = misc.imread(f1)
    imgtest=misc.imread(f1)
    #storing old version
    imgold = misc.imread(f1)
    print(len(img))
    #print(img[0][0])
    #print(img)



#=================================================================================
    #         Get the filename as string
    f2 = "desync2.pgm"
    #         Read file it np array
    img2 = misc.imread(f2)
    #storing old version
    img2old = misc.imread(f2)
    print(len(img2))
    #print(img[0][0])
    #print(img)


#=================================================================================
    #         Get the filename as string
    f3 = "desync3.pgm"
    #         Read file it np array
    img3 = misc.imread(f3)
    #storing old version
    img3old = misc.imread(f3)
    print(len(img3))
    #print(img[0][0])
    #print(img)

#=================================================================================
    #         Get the filename as string
    f4 = "desync4.pgm"
    #         Read file it np array
    img4 = misc.imread(f4)
    #storing old version
    img4old = misc.imread(f4)
    print(len(img4))
    #print(img[0][0])
    #print(img)


    '''

    #2dfft
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    '''
    '''
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    '''
    f1d=[]
    for row in img:
        #print(row)
        fnewrow = np.fft.fft(row)
        fnewshift = np.fft.fftshift(fnewrow)
        
        #print(fnewshift)
        f1d.append(fnewshift)
    #phase correlation function taking two rows from image file
    #returns the position of the peak of the correlation
    def corr(row1,row2):
        ft = np.fft.fft(row1)
        fshift= np.fft.fftshift(ft)
        fcom= np.conj(fshift)
        ft2 = np.fft.fft(row2)
        fshift2= np.fft.fftshift(ft2)
        mult = np.multiply(fcom,fshift2)
        imult= np.fft.ifft(mult)
        return(np.argmax(imult))

    #def opcorr(row1,row2)
    '''
    def multicorr(row1,row2,row3,row4):
        '''
        ft1=np.fft.fft(row1)
        fshift1=np.fft.fftshift(ft1)
        ft2=np.fft.fft(row2)
        fshift2=np.fft.fftshift(ft2)
        ft3=np.fft.fft(row3)
        fshift3=np.fft.fftshift(ft3)
        '''
        #looking at shifting row 2 back
        val = int((corr(row2,row3)+corr(row1,row2)))#negative because its looking backwards
        return val
    '''    
    shitvals=[]
    for i in range(len(img)-1):
        if i == 0 or i>=(len(img)-4):
            continue
        else:
            val=multicorr(img[i],img[i+1],img[i+2],img[i+2])
            print(val)
            img[i+1]=np.roll(img[i+1],-val)
    print(shitvals)
        #print(i)
    '''
        if (len(img)-7)<=i<=(len(img)-1):
            print(i)
            val = corr(img[i],img[i+1])
            img[i+1]=np.roll(img[i+1],-val)
        elif i<2:
            continue
        else:
            print("lol" '{}'.format(i))
            valnew = multicorr(imgtest[i],imgtest[i+1],imgtest[i+2],imgtest[i+3],imgtest[i+4])
            imgtest[i+2]=np.roll(imgtest[i+2],-valnew)
        #else:
        '''
        
    for i in range(len(img2)-1):
        val2=corr(img2[i],img2[i+1])
        img2[i+1]=np.roll(img2[i+1],-val2)
    for i in range(len(img3)-1):
        val3=corr(img3[i],img3[i+1])
        img3[i+1]=np.roll(img3[i+1],-val3)
    for i in range(len(img4)-1):
        val4=corr(img4[i],img4[i+1])
        img4[i+1]=np.roll(img4[i+1],-val4)
        
    #mag_spec = 20*np.log(np.abs(f1d))

    
    #calculating complex conjugates
    #fconj=[]
    #vals=[]


    '''
    for i in range(len(f1d)-1):
        #val = np.conj(f1d[i])#conj i 
        #fconj.append(val)
        tempval = (np.fft.ifft(np.multiply(np.conj(f1d[i]),f1d[i+1])))#calc dist
        shift=-1*np.argmax(tempval)#dist max
        print(shift)
        #rolling
        img[i+1]=np.roll(img[i+1],shift)#rolling line i+1
    
    '''
        #print(fconj)
        #print(f1d)
    #shiftvals=[]
    #val =[]
    #ival = []
    #now comparing lines
    #newimage=[]
    '''
    for i in range(len(f1d)-1):
        
        val.append(np.fft.ifft(np.multiply(fconj[i],f1d[i+1])))
        shiftval=np.argmax(val[i])
        #print(shiftval)
        shiftvals.append(shiftval)
        #print(img[i])
        temp = img[i+1]
        img[i+1]=np.roll(img[i+1],-1*shiftval)#need to roll backwards otherwise we are going in the same direction again 
        tempnew= np.subtract(img[i+1],temp)
        print(tempnew)
        #print(img[i])
    '''
    '''
    '''
    
    
        
        
        #val[i] = np.fft.ifft[val[i]]
        #print(val[i])
        #shiftvals.append(ival)
    #print(val)
    
    '''
    for i in range(len(val)):
        shiftvals.append(np.argmax(val[i]))
        img[i]
    print(shiftvals)
    

    for row in img:
        count=0
        #    if shiftvals[i] > len(img):
        #       np.roll(shiftvals[i],len(img))
        #if shiftvals[i]>len(img):
            #diff = shiftvals[i]-len(img)
            #np.roll(img,shiftvals[i])
        #else:
        np.roll(row,shiftvals[count])
        count+=1
    '''

    '''
    plt.imshow(img, cmap = 'gray')
    plt.title('Output Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    #plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    '''
    '''
    plt.subplot(121),plt.imshow(imgold, cmap = 'gray')
    plt.title('input Image 1'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(imgtest, cmap = 'gray')
    plt.title('output Image 1'), plt.xticks([]), plt.yticks([])
    plt.show()
    '''
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Output Image 1'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(imgold, cmap = 'gray')
    plt.title('Input Image 1'), plt.xticks([]), plt.yticks([])
    plt.show()

    plt.subplot(121),plt.imshow(img2, cmap = 'gray')
    plt.title('Output Image 2'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2old, cmap = 'gray')
    plt.title('Input Image 2'), plt.xticks([]), plt.yticks([])
    plt.show()

    plt.subplot(121),plt.imshow(img3, cmap = 'gray')
    plt.title('Output Image 3'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img3old, cmap = 'gray')
    plt.title('Input Image 3'), plt.xticks([]), plt.yticks([])
    plt.show() 

    plt.subplot(121),plt.imshow(img4, cmap = 'gray')
    plt.title('Output Image 4'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img4old, cmap = 'gray')
    plt.title('Input Image 4'), plt.xticks([]), plt.yticks([])
    plt.show()

    #print(shiftvals)
    
    #comparing three lines
    #now we want to find the position of the pak
    
    '''
    
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(122),plt.imshow(mag_spec, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    
    length = len(f1d)
    corre = []
    for i in range(length -1):
        val = np.inner(f1d[i],f1d[2])
        #newval = abs(val)
        corre.append(val)
    #print(corre)

    
    correvals = []
    for i in range(len(corre)):
        inv = np.fft.ifft(row).real
        #print(inv)
        correvals.append(inv)
    #print (correvals))
    xvals=[i for i in range(len(correvals))]
    
    plt.plot(xvals,correvals)
    plt.show()
    '''

    


main()
