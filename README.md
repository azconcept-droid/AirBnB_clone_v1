# 0x01. AirBnB clone - Console
``CLI`` ``BACKEND``

Project description
===
### The console
<ul>
    <li>create your data model</li>
    <li>manage (create, update, destroy, etc) objects via a console / command interpreter</li>
    <li>store and persist objects to a file (JSON file)</li>
</ul>

<p> The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.</p>

<p> This abstraction will also allow you to change the type of storage easily without updating all of your codebase.</p>

<p> The console will be a tool to validate this storage engine</p>

**Resources**
- [Python cmd module](https://docs.python.org/3.8/library/cmd.html)
- [Python cmd module in depth](http://pymotw.com/2/cmd/)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime module](https://docs.python.org/3.8/library/datetime.html)
- [ Flask Mega-Tutorial series](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
