# Configuration
The script is running on python `3.9.13`

# Client's need

**The problem:** The client wants to download a zoomed image from a website, at the highest resolution, which is divided into 69x53 pieces of 255x255 pixels. It is not possible to access this image because zooms usually use JavaScript. 

Images loaded via JavaScript do not exist in the HTML page - the whole web page record only records the images that load when the page is loaded.. 

**Solution:** 
- Identify the root link of the images and the number of pieces to download.
- Create a script to download all 3000+ images at once. 

**TO DO:** 
- Use a rotating proxy


