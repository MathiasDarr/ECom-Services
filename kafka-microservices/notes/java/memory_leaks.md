### Memory Leaks ###

Standard definition of memory leaks
scenario that occurs when objects are no longer being used by the application, but the garbage collector is unable to
remove them from working memory, because they are being referenced.  
OutOfMemoryError

Two types of objects
 - referenced and unreferenced
garbage collector can remove objects that are being unreferenced.  referenced objects won't be collected,   

Memory leak scenarios

Static field holding on to the object reference

referencying a heavy object w/ a static field 