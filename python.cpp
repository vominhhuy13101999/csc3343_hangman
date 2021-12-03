#define PY_SSIZE_T_CLEAN

#include <Python.h>
// #include "search.h"
#include <string>
#include "search.cpp"
// #include "bf_search.tpp"    

using namespace std;


string* arr=read_dataset("./text.txt");
int size=370099;

static PyObject *SearchError;
static char search_doc[] =
   "search.bf( string)\n search.bst( string)\nsearch.cs( string)\n";
static PyObject * search_bf(PyObject *self, PyObject *args)
{
    const char *a;
    int index=0;
    if (!PyArg_ParseTuple(args, "s", &a)) //how the function received value from python
        return NULL;
    string a_(a);

    index = bf_search<string>(arr,size,a_); //perform code here example perform 
    // cout<<command<<endl;
    if (index < 0) {
        PyErr_SetString(SearchError, "Search failed");
        return PyLong_FromLong(index);
    }
    return PyLong_FromLong(index); // how function return value in python
};

static PyObject * search_bst(PyObject *self, PyObject *args)
{
    const char *a;
    int index=0;
    if (!PyArg_ParseTuple(args, "s", &a)) //how the function received value from python
        return NULL;
    string a_(a);

    index = bst_search<string>(arr,0,size-1,a_); //perform code here example perform 
    // cout<<command<<endl;
    if (index < 0) {
        PyErr_SetString(SearchError, "Search failed");
        return PyLong_FromLong(index);
    }
    return PyLong_FromLong(index); // how function return value in python
};
static PyObject * search_cs(PyObject *self, PyObject *args)
{
    const char *a;
    int index=0;
    if (!PyArg_ParseTuple(args, "s", &a)) //how the function received value from python
        return NULL;
    string a_(a);

    index = cs_search<string>(arr,size,a_); //perform code here example perform 
    // cout<<command<<endl;
    if (index < 0) {
        PyErr_SetString(SearchError, "Search failed");
        return PyLong_FromLong(index);
    }
    return PyLong_FromLong(index); // how function return value in python
};

static PyObject * get_value(PyObject *self, PyObject *args)
{
    int a;
    char *v_;
    if (!PyArg_ParseTuple(args, "i", &a)) //how the function received value from python
        return NULL;
    v_ = &(*(arr+a))[0]; //perform code here example perform 

    return Py_BuildValue("s",v_); // how function return value in python
};

//lists all method
static PyMethodDef SearchMethods[] = {
    {"bf",  search_bf, METH_VARARGS,
     "Execute a brute force search."},
    {"bst", search_bst, METH_VARARGS, 
    "Execute a binary search tree."},   
    {"cs", search_cs, METH_VARARGS, 
    "Execute a decrease by constant."}, 
    {"get_value", get_value, METH_VARARGS, 
    "return value byy index"},
    {NULL, NULL, 0, NULL},     /* Sentinel */
};


//initialize module
static struct PyModuleDef searchmodule = {
    PyModuleDef_HEAD_INIT,
    "search",   /* name of module */
    search_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SearchMethods
};

PyMODINIT_FUNC
PyInit_search(void)
{
    PyObject *m;

    m = PyModule_Create(&searchmodule);
    if (m == NULL)
        return NULL;

    SearchError = PyErr_NewException("search.error", NULL, NULL); // create class of exception in python
    Py_XINCREF(SearchError);
    if (PyModule_AddObject(m, "error", SearchError) < 0) {
        Py_XDECREF(SearchError);
        Py_CLEAR(SearchError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}