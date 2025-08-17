# 17842726 - Hespik-Fespik

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Yahse Hunting Grounds (ID: 260) |
| Block Size       | 228 bytes                       |
| Total Events     | 7                               |
| References Count | 12                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [507](#event-507)        | 0x0001       |     43 |              9 |
| [65535.1](#event-655351) | 0x002C       |      1 |              1 |
| [65535.2](#event-655352) | 0x002D       |     16 |              2 |
| [65535.3](#event-655353) | 0x003D       |     29 |              3 |
| [65535.4](#event-655354) | 0x005A       |     24 |              3 |
| [65535.5](#event-655355) | 0x0072       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0031      |          49 |
|       1 | 0x1EBD      |        7869 |
|       2 | 0x0045      |          69 |
|       3 | 0x0008      |           8 |
|       4 | 0x0000      |           0 |
|       5 | 0x00E1      |         225 |
|       6 | 0x0066      |         102 |
|       7 | 0x0001      |           1 |
|       8 | 0x0005      |           5 |
|       9 | 0x0014      |          20 |
|      10 | 0x008E      |         142 |
|      11 | 0x0039      |          57 |

## String References

- **7869**: This Yahse-Wahse Battlegrounds pioneering business sure is tough!

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

### Event 507

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 66 00 80 F8 FF  ...tlk0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7869*)
    → "This Yahse-Wahse Battlegrounds pioneering business sure is tough!"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         66 02 80               f..
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 02 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 53 F8 FF FF  ........tlk1S...
0050: 7F F8 FF FF 7F 74 65 6E  30 00                    .....ten0.      
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=69*
  1: 0x004C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ten0" with entities [EventEntity, EventEntity]
  2: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                B6 0B 03 80 04 80            ......
0060: 04 80 05 80 05 80 06 80  06 80 04 80 04 80 C0 07  ................
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x005A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=0*, head=0*, body=225*, hands=225*, legs=102*, feet=102*, main=0*, sub=0*)
  1: 0x006E [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       B6 0B 08 80 07 80  09 80 0A 80 04 80 0B 80    ..............
0080: 0B 80 04 80 04 80 00                              .......         
```

#### Opcodes

```
  0: 0x0072 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=1*, head=20*, body=142*, hands=0*, legs=57*, feet=57*, main=0*, sub=0*)
  1: 0x0086 [0x00] END_REQSTACK()
```
