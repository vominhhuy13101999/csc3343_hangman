#define PY_SSIZE_T_CLEAN

#include <Python.h>
// #include "search.h"
#include <string>
#include "search.cpp"
// #include "bf_search.tpp"    
#include <vector>
#include <typeinfo>
#include <stdexcept>

using namespace std;



//_______________________________________________________________________________


// =====
// LISTS
// =====

PyObject* vectorToList_Float(const vector<double> &data) {
  PyObject* listObj = PyList_New( data.size() );
	if (!listObj) throw logic_error("Unable to allocate memory for Python list");
	for (unsigned int i = 0; i < data.size(); i++) {
		PyObject *num = PyFloat_FromDouble( (double) data[i]);
		if (!num) {
			Py_DECREF(listObj);
			throw logic_error("Unable to allocate memory for Python list");
		}
		PyList_SET_ITEM(listObj, i, num);
	}
	return listObj;
}
PyObject* vectorToList_Int(const vector<int> &data) {
  PyObject* listObj = PyList_New( data.size() );
	if (!listObj) throw logic_error("Unable to allocate memory for Python list");
	for (unsigned int i = 0; i < data.size(); i++) {
		PyObject *num = PyLong_FromLong( (int) data[i]);
		if (!num) {
			Py_DECREF(listObj);
			throw logic_error("Unable to allocate memory for Python list");
		}
		PyList_SET_ITEM(listObj, i, num);
	}
	return listObj;
}
// ======
// TUPLES
// ======

PyObject* vectorToTuple_Float(const vector<float> &data) {
	PyObject* tuple = PyTuple_New( data.size() );
	if (!tuple) throw logic_error("Unable to allocate memory for Python tuple");
	for (unsigned int i = 0; i < data.size(); i++) {
		PyObject *num = PyFloat_FromDouble( (double) data[i]);
		if (!num) {
			Py_DECREF(tuple);
			throw logic_error("Unable to allocate memory for Python tuple");
		}
		PyTuple_SET_ITEM(tuple, i, num);
	}

	return tuple;
}

PyObject* vectorVectorToTuple_Float(const vector< vector< float > > &data) {
	PyObject* tuple = PyTuple_New( data.size() );
	if (!tuple) throw logic_error("Unable to allocate memory for Python tuple");
	for (unsigned int i = 0; i < data.size(); i++) {
		PyObject* subTuple = NULL;
		try {
			subTuple = vectorToTuple_Float(data[i]);
		} catch (logic_error &e) {
			throw e;
		}
		if (!subTuple) {
			Py_DECREF(tuple);
			throw logic_error("Unable to allocate memory for Python tuple of tuples");
		}
		PyTuple_SET_ITEM(tuple, i, subTuple);
	}

	return tuple;
}

// PyObject -> Vector
vector<double> listTupleToVector_Float(PyObject* incoming) {
	vector<double> data;
	if (PyTuple_Check(incoming)) {
		for(Py_ssize_t i = 0; i < PyTuple_Size(incoming); i++) {
			PyObject *value = PyTuple_GetItem(incoming, i);
			data.push_back( PyFloat_AsDouble(value) );
		}
	} else {
		if (PyList_Check(incoming)) {
			for(Py_ssize_t i = 0; i < PyList_Size(incoming); i++) {
				PyObject *value = PyList_GetItem(incoming, i);
				data.push_back( PyFloat_AsDouble(value) );
			}
		} else {
			throw logic_error("Passed PyObject pointer was not a list or tuple!");
		}
	}
	return data;
}

// PyObject -> Vector
vector<int> listTupleToVector_Int(PyObject* incoming) {
	vector<int> data;
	if (PyTuple_Check(incoming)) {
		for(Py_ssize_t i = 0; i < PyTuple_Size(incoming); i++) {
			PyObject *value = PyTuple_GetItem(incoming, i);
			data.push_back( PyFloat_AsDouble(value) );
		}
	} else {
		if (PyList_Check(incoming)) {
			for(Py_ssize_t i = 0; i < PyList_Size(incoming); i++) {
				PyObject *value = PyList_GetItem(incoming, i);
				data.push_back( PyFloat_AsDouble(value) );
			}
		} else {
			throw logic_error("Passed PyObject pointer was not a list or tuple!");
		}
	}
	return data;
}











































//_______________________________________________________________________________

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

static PyObject * avltree(PyObject *self, PyObject *args)
{
    Py_ssize_t i = 0;
    PyObject* o= PyTuple_GetItem(args,i);
    vector<double> v=listTupleToVector_Float( o);
    int index=0;

    avlTree* T=new avlTree();
    T->head=NULL;

    pair<double,int> p;
    for(double& i:v){
        p= make_pair(i,index);
        T->head= T->insert(T->head,p );
        ++index;
    }
    // T->preorder(T->head);

    // index = cs_search<string>(arr,size,a_); //perform code here example perform 
    // // cout<<command<<endl;
    // if (index < 0) {
    //     PyErr_SetString(SearchError, "Search failed");
    //     return PyLong_FromLong(index);
    // }
    vector<int> v1=T->extract_5_min(T->get_5_min(T->head));

    return  vectorToList_Int(v1); // how function return value in python
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
    {"avl", avltree, METH_VARARGS, 
    "avl tree and stuff"},
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