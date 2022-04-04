# General
Creating my own cheat toolkit.

# External Cheats */
external cheats, reads memory to get player position.

# Read Process Memory */
[!docs](https://msdn.microsoft.com/en-gb/library/windows/desktop/ms680553(v=vs.85).aspx)

```csharp

// success = return nonzero
// fail = return 0
/*------------------------
- success = return nonzero
- fail = return 0
Param 1: PID
    ProcessHandle from OpenProcess
Param 2: Base Adress
    Target Memory Address - in target process
Param 3: Buffer
    Storage in memory or buffer in memory
    
    
------------------------*/
BOOL ReadProcessMemory(
  [in]  HANDLE  hProcess, // Process
  [in]  LPCVOID lpBaseAddress, # What adress to read.
  [out] LPVOID  lpBuffer, # where the info gets stored after reading
  [in]  SIZE_T  nSize, # bytes?
  [out] SIZE_T  *lpNumberOfBytesRead # don't need.
);
```

```csharp

// Update
BOOL WINAPI ReadProcessMemory(
    _In_  HANDLE  hProcess, // OpenProcess Handle
    _In_  LPCVOID lpBaseAddress,
    _Out_ LPVOID  lpBuffer,
    _In_  SIZE_T  nSize,
    _Out_ SIZE_T  *lpNumberOfBytesRead
);
```



```csharp
/*--------------------------------
Param 1: 
    What Access we Request..
Param 2:
    Don't really care
Param 3: PID
    Process ID, Task-manager
---------------------------------*/
// OpenProcess
HANDLE WINAPI OpenProcess(
    _In_ DWORD dwDesiredAccess,
    _In_ BOOL  bInheritHandle,
    _In_ DWORD dwProcessId
);


```