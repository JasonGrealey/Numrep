from scipy import misc
import matplotlib.pyplot as plt
import numpy as np 
import math

def main():
    #         Get the filename as string
    #fn = str(raw_input("File : "))
    fn = "desync4.pgm"
    #         Read file it np array
    img = misc.imread(fn)
    imgold = misc.imread(fn)
    print(len(img))
    print(img[0][0])
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

    def corr(row1,row2):
        ft = np.fft.fft(row1)
        fshift= np.fft.fftshift(ft)
        fcom= np.conj(fshift)
        ft2 = np.fft.fft(row2)
        fshift2= np.fft.fftshift(ft2)
        mult = np.multiply(fcom,fshift2)
        imult= np.fft.ifft(mult)
        return(np.argmax(imult))

    for i in range(len(img)-1):
        val = corr(img[i],img[i+1])
        #print(val)
        img[i+1]=np.roll(img[i+1],-val)
        
        
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
    shiftvals=[]
    val =[]
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
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Output Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(imgold, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
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
