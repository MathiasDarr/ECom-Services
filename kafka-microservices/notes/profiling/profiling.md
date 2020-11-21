Debugging performance issues in production can be a pain and, in some cases, impossible without the right tools. Java profiling has been around forever, but the java profilers most developers think about are only one type: standard JVM profilers.

However, using one type of profiler is not enough.

Suppose you’re analyzing your application’s performance. There are multiple profiling activities which you may execute. Generally, standard profilers handle memory profiling, CPU profiling, and thread profiling.

But even with all this coverage, by using a combination of multiple profilers, you’ll find more performance issues. This is because each profiler is better in a certain aspect for chasing a performance bug.