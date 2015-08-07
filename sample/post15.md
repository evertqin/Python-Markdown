
1. This is a title

      Some nested code blocks

2. Also Test

      The C++ source files need to be specially wrapped to expose function interfaces to managed code: in the header file: (headers.hh), need to
* Wrap all the function signatures in `extern "C"` because we don't want C++ compiler to mangle the function name.
* append `__declspec(dllexport)` before function declearation.

      a basic example, first creat an empty C++ dll project and add two files: headers.hh and source.cc. In header.hh file, add the following lines:

            ~~~~{.cpp}
#ifndef CPPLIB_HEADERS_HH
#define CPPLIB_HEADERS_HH

extern "C"
{
	__declspec(dllexport) void get_simple_type(int num);
}

#endif
            ~~~~


~~~~{.csharp}
[DllImport("CppLib.dll")]
public static extern IntPtr make_1d_array(double[] nums, int size);
[DllImport("CppLib.dll")]
public static extern int release_one_dim(IntPtr toFree);

public void RetriveArrayType()
{
    Console.WriteLine("Retriving Array");
    double[] nums = { 1, 2, 3, 4, 5 };
    IntPtr ptr = make_1d_array(nums, nums.Length);
    OneDimRetArray result = (OneDimRetArray)Marshal.PtrToStructure(ptr,
                            typeof(OneDimRetArray));

    double[] num = new double[result.size];
    Marshal.Copy(result.content, num, 0, result.size);
    foreach (double d in num)
    {
        Console.Write(d + ", ");
    }
    Console.WriteLine();

    int release = release_one_dim(ptr);
}
~~~~

Run the whole project, you should see the following output.
![Run Result](/home/ruogu/Pictures/Capture.PNG)
