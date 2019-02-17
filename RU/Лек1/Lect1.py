
# coding: utf-8

# In[2]:


from skimage.io import imread, imsave, imshow
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


im = imread('parrot.png')
imshow(im)


# In[4]:


im.shape


# In[5]:


im.shape[1]


# In[6]:


im[384, 356]


# In[7]:


im[384, 356] = [255, 255, 0]


# In[8]:


imshow(im)


# In[9]:


imsave('parrot_pix.png', im)


# In[10]:


beak = im[300:650, 950:1300]


# In[11]:


imshow(beak)


# In[12]:


im[300:650, 950:1300] = [255, 0, 255]


# In[13]:


imshow(im)


# In[14]:


im = imread('parrot.png')


# In[15]:


img_assigned = im


# In[16]:


img_copy = im.copy()


# In[17]:


img_assigned[300:650, 950:1300] = [255, 0, 255]


# In[18]:


imshow(im)


# In[19]:


imshow(img_assigned)


# In[20]:


imshow(img_copy)


# In[21]:


im = imread('parrot.png')
imshow(im)


# In[22]:


im.dtype


# In[23]:


r = im[:,:,0]
imshow(r)


# In[24]:


g = im[:,:,1]
imshow(g)


# In[25]:


b = im[:,:,2]
imshow(b)


# In[26]:


from numpy import dstack
img_combined = dstack((r,g,b))
img_combined.shape


# In[27]:


imshow(img_combined)


# In[28]:


imshow(dstack((g,b,r)))


# In[30]:


from skimage import img_as_float 


# In[31]:


img_f = img_as_float(im)


# In[32]:


img_f.min(), img_f.max()


# In[33]:


im.min(), im.max()


# In[34]:


imshow(img_f / 1.5)


# In[35]:


imshow(img_f / 2)


# In[36]:


imshow(img_f / 4)


# In[37]:


imshow(img_f / 4 + 0.4)


# In[38]:


from numpy import clip


# In[39]:


imshow(clip(img_f * 1.5, 0, 1))


# In[40]:


imshow(clip(img_f * 2, 0, 1))


# In[41]:


imshow(clip(img_f * 2 - 0.5, 0, 1))


# In[43]:


img = imread('parrot.png')
img_f = img_as_float(img)
r = img_f[:,:,0]
g = img_f[:,:,1]
b = img_f[:,:,2]
imshow((r + g + b) / 3)

