# 17723515 - Ronpaurege

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 212 bytes                     |
| Total Events     | 10                            |
| References Count | 3                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              2 |
| [65535.2](#event-655352) | 0x0012       |     22 |              4 |
| [65535.3](#event-655353) | 0x0028       |     16 |              2 |
| [65535.4](#event-655354) | 0x0038       |     14 |              2 |
| [65535.5](#event-655355) | 0x0046       |     16 |              2 |
| [65535.6](#event-655356) | 0x0056       |     14 |              2 |
| [65535.7](#event-655357) | 0x0064       |      9 |              3 |
| [669](#event-669)        | 0x006D       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1C71      |        7281 |
|       2 | 0x1C72      |        7282 |

## String References

- **7281**: It's been twenty years since my son joined the Temple Knights... And still Ronfaure is thick with Orcs!
- **7282**: It's all the fault of those Royal Knights! Does Prince Trion think to undo all that my son has wrought? Does he?

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    [..........tlk
0010: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0002 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 5E    S........tlk0^
0020: 69 64 6C 30 1C 00 80 00                           idl0....        
```

#### Opcodes

```
  0: 0x0012 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0024 [0x1C] WAIT(30* ticks)
  3: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          5B 00 80 F8 FF FF 7F F8          [.......
0030: FF FF 7F 74 68 6B 31 00                           ...thk1.        
```

#### Opcodes

```
  0: 0x0028 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          53 F8 FF FF 7F F8 FF FF          S.......
0040: 7F 74 68 6B 31 00                                 .thk1.          
```

#### Opcodes

```
  0: 0x0038 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
0050: 7F 74 68 6B 32 00                                 .thk2.          
```

#### Opcodes

```
  0: 0x0046 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   53 F8  FF FF 7F F8 FF FF 7F 74        S........t
0060: 68 6B 32 00                                       hk2.            
```

#### Opcodes

```
  0: 0x0056 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             5E 69 64 6C  30 1C 00 80 00               ^idl0....   
```

#### Opcodes

```
  0: 0x0064 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0069 [0x1C] WAIT(30* ticks)
  2: 0x006C [0x00] END_REQSTACK()
```

### Event 669

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         1E F0 FF               ...
0070: FF 7F 6F 70 29 08 7B 70  0E 01 02 1D 01 80 23 1D  ..op).{p......#.
0080: 02 80 23 29 08 7B 70 0E  01 03 20 00 21 00        ..#).{p... .!.  
```

#### Opcodes

```
  0: 0x006D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0072 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0073 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0074 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ronpaurege (ID: 17723515/0x010E707B), tag_num=0x02)
  4: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=7281*)
    → "It's been twenty years since my son joined the Temple Knights... And still Ronfaure is thick with Orcs!"
  5: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=7282*)
    → "It's all the fault of those Royal Knights! Does Prince Trion think to undo all that my son has wrought? Does he?"
  7: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0083 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Ronpaurege (ID: 17723515/0x010E707B), tag_num=0x03)
  9: 0x008A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x008C [0x21] END_EVENT
 11: 0x008D [0x00] END_REQSTACK()
```
