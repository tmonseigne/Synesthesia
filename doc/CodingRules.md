# Coding Rules

## Git Rules
One main thing/feature per commit (unless you document your code at the same time as you code).  
Use of [Git Emoji](https://gitmoji.carloscuesta.me/) (if you need two git emoji [except documentation] try to split your commit) 

## Repository Structure

- **audio** : For samples
- **dependencies** : installed dependencies   
- **doc** For Documentation complement, Doxyfile, coding rules...
	- only in *.md for text
	- Documentation images : prefers Vector graphics *.svg or *.png
	- *Logo* : synesthesia.svg & synesthesia.png
- **images** : If Images needed (not for documentation)
- **src** : all source code except tests
	- **gui** : standalone interface
		- **.hpp*, **.cpp*, *CMakeLists.txt*
	- **sound-processing** : all sound processing
		- **.hpp*, **.cpp*, *CMakeLists.txt*
	- **visualization** : visualization
		- **.hpp*, **.cpp*, *CMakeLists.txt*
	- *CMakeLists.txt* 
- **tests**  
	all tests source code
	- **.hpp*, **.cpp*, *CMakeLists.txt*
- *.gitignore*
- *LICENSE*
- *README.md*
- *build.cmd*
- *build.sh* 
- *install_dependencies.cmd*
- *install_dependencies.sh* 


## folders and files name
- **Folders** :  
all-lower
	- &#10004; **my-folder-name**
	- &#10060; **my_folder_name**, **myFolderName**, **MyFolderName**, **My Folder Name**...
- *Files* :  
lowerCamelCase, UpperCamelCase, Underscore prefix tolerant, dash + specification suffix tolerant 
	- &#10004; *myFileName.ext*, *MyFileName.ext*, *myFileName-extended.ext*, *_myFileName.ext* 
	- &#10060; *my_file_name*, *my-file-name*, *My File Name*...

## C/C++ Coding Rules

### Naming
#### Explicit Naming
The name should be explicit. Abbreviations are allowed as long as they are obvious.  
Ex: pointer => ptr, input => in, result => res...  

#### Naming Style
| Entity | Style | Prefix | Suffix | Naming Template |
|:---|:---|:---:|:---:|:---|
| Struct | UpperCamelCase | S | | SMyStruct |
| Enum | UpperCamelCase | E | | EMyEnum |
| Class | UpperCamelCase | C | | CMyClass |
| Template class | UpperCamelCase | T | | TMyTemplateClass |
| Interface (abstract class) | UpperCamelCase | I | | IMyInterface |
| Local Function (in cpp) | lowerCamelCase | | | myFunction |
| Global Function (in hpp) | UpperCamelCase | | | MyFunction |
| Function argument | all_lower | | | my_args |
| CONST | ALL_UPPER | | | MY_CONST |
| **Class/struct** |  |  |  |  |
| - Private variable | lowerCamelCase | _ | | _myVariable |
| - Public variable | UpperCamelCase | _ | | _MyVariable |
| - Private Function | lowerCamelCase | | | myFunction |
| - Public Function | UpperCamelCase | | | MyFunction |

### Modernize style Code
In Header file :  
&#10004; `#pragma once`  
&#10060; `#ifndef ...#define ... #endif`

auto use : 
use auto if type is iterator or not important  
&#10004; `for (const auto& elem:vector){ cout<<elem; }`  
&#10004; `auto it = v.begin();`  
&#10060; `auto i = 0;`


Loop with useless iterator :  
&#10004; `for (const auto& elem:vector){ cout<<elem; }`  
&#10060; `for (size_t i = 0; i < vector.size(); ++i){ cout<<vector[i]; }`  
&#10060; `for (auto it = v.begin(); it != v.end(); ++it){ cout<<*it; }`  

nullptr instead of NULL:  
&#10004; `double *a = nullptr;`  
&#10060; `double *a = NULL;`  

always initialize the variables in the class declaration : 
```
class C
{
public:
	int var = 0;
	float *arr = nullptr; 

	void a();
};
```

#### Class declaration
```
class C
{
protected:
	//variables (const first)
private:
	//variables (const first)
public:
	//variables (const first)
protected:
	//function
private:
	//function
public:
	//function
};
```


### Formatting 
It's a listing of Resharper options (plugin of Jetbrain in visual studio). If you use it you can load the setting file in `doc` folder

#### Tabs & Indent
- Tab character
- How to aligne : Mix Tab and space for optimal fill

#### Braces Layout
**Namespace Déclaration** : at next line (BSD Style)

```
namespace ns
{
	void a();
}
```
**Type Declaration** : at next line (BSD Style)  
```
class C
{
public:
	void a();
};
```
**Place Namespace on the same line** : false
```
namespace A
{
	namespace B
	{
		void a();
	}
}
```
**Function Déclaration** : at next line (BSD Style)
```
void a()
{
	b();
}
```
**Block under case label** : at end of line (K&R Style)  
```
switch (expression) {
	case 0: {
		foo();
		break;
	}
}
```
**Other statement and blocks** : at end of line (K&R Style)  
```
if (condition) {
	foo();
} else {
	foo();
}
```

**Empty Braces format** : together on the same line (BSD Style)  

```
class C {};
```

**Simple statement** : as you want short statement can be stay in one line
```
int foo() { return 0; }
int foo()
{
	return 0;
}
```

#### Blank lines
**Max blank lines** : 1  
**Blank line around function, namespace, classes** : min 1  
**Blank line around variable declaration** : min 0

#### Spaces
**pointer & reference declaration** : before
```
int **data;
int **data, *data2, &data3 = *data2;
int **foo(int a, int b);
```

**comma déclaration** : before
```
int a, b, c;
int foo(int a, int b, int c);
template<typename K, typename V>
```

**parentheses parameter, angle bracket Template, empty bracket** : No
```
int foo(int a, int b, int c);
template<typename K>
vector<vector<int>> v;
template<>
int foo();
struct map {};
```

**around operator** : Always
```
c = a + b;
c = (a > 0) ? a : b; 
```

**Align end of line comments if possible**
```
int a;			// a variable
int FooVariable;	// Foo Variable
```

**Align Multiple declaration if possible** : previous option in Tabs & Indent part make for you the alignment
```
int first,
    second;
double average(double first,
	       double second);
```

#### Line breaks

**If / else** : if single statement : as you want short statement can be stay in one line
```
if (true) {
	foo();
} else {
	foo();
}

if (true) { foo(); }
else { foo(); }
```

**Do While** :
```
do {
	foo();
} while (true);
```

**Try Catch** :
```
try {
	foo();
} catch (...) {
	foo();
}
```

**Switch Case** : if single statement : as you want short statement can be stay in one line
```
switch (a) {
	case b: 
		foo(); 
		foo(); 
		break;
	case c: break;
}

switch (a) {
	case b: foo(); break;
	case c: foo(); break;
}
```

