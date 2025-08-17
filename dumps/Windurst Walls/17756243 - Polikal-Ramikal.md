# 17756243 - Polikal-Ramikal

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 320 bytes                |
| Total Events     | 12                       |
| References Count | 9                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     16 |              2 |
| [65535.3](#event-655353) | 0x0021       |     14 |              2 |
| [65535.4](#event-655354) | 0x002F       |     16 |              2 |
| [65535.5](#event-655355) | 0x003F       |     14 |              2 |
| [65535.6](#event-655356) | 0x004D       |     16 |              2 |
| [65535.7](#event-655357) | 0x005D       |     14 |              2 |
| [65535.8](#event-655358) | 0x006B       |      9 |              3 |
| [443](#event-443)        | 0x0074       |      7 |              2 |
| [320](#event-320)        | 0x007B       |     33 |             12 |
| [391](#event-391)        | 0x009C       |     63 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x0029      |          41 |
|       2 | 0x001E      |          30 |
|       3 | 0x1EFF      |        7935 |
|       4 | 0x1F00      |        7936 |
|       5 | 0x227F      |        8831 |
|       6 | 0x2280      |        8832 |
|       7 | 0x0001      |           1 |
|       8 | 0x2281      |        8833 |

## String References

- **7935**: Hmm... Tsk-tsk... This is more serious-derious than I thought-dought...
- **7936**: ...Ah? ...Oh! ...Huh? If you're looking-dooking for the entrance to Heavens Tower, it's on the other side-dide of this poor old star tree that encases it.
- **8831**: ...Oh, $6! You have Rhinostery authorization-nation.
- **8832**: ...I heard aboutaru the theory that the withering-dithering of the Star Tree is caused by insects chewing-zewing on the roots.
- **8833**: We'll leave the extermination-termination of the bugs in your capable hands.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   f..........thk1
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00      S........thk1. 
```

#### Opcodes

```
  0: 0x0021 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               66                 f
0030: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     ..........thk2. 
```

#### Opcodes

```
  0: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               53                 S
0040: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x003F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         66 01 80               f..
0050: F8 FF FF 7F F8 FF FF 7F  73 68 6B 30 00           ........shk0.   
```

#### Opcodes

```
  0: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         53 F8 FF               S..
0060: FF 7F F8 FF FF 7F 73 68  6B 30 00                 ......shk0.     
```

#### Opcodes

```
  0: 0x005D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   5E 69 64 6C 30             ^idl0
0070: 1C 02 80 00                                       ....            
```

#### Opcodes

```
  0: 0x006B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0070 [0x1C] WAIT(30* ticks)
  2: 0x0073 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x0074 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 320

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   29 0B 53 F0 0E             ).S..
0080: 01 01 1D 03 80 23 1E F0  FF FF 7F 6F 70 1D 04 80  .....#.....op...
0090: 23 29 0B 53 F0 0E 01 08  20 00 21 00              #).S.... .!.    
```

#### Opcodes

```
  0: 0x007B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polikal-Ramikal (ID: 17756243/0x010EF053), tag_num=0x01)
  1: 0x0082 [0x1D] PRINT_EVENT_MESSAGE(message_id=7935*)
    → "Hmm... Tsk-tsk... This is more serious-derious than I thought-dought..."
  2: 0x0085 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0086 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x008B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x008C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=7936*)
    → "...Ah? ...Oh! ...Huh? If you're looking-dooking for the entrance to Heavens Tower, it's on the other side-dide of this poor old star tree that encases it."
  7: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0091 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polikal-Ramikal (ID: 17756243/0x010EF053), tag_num=0x08)
  9: 0x0098 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x009A [0x21] END_EVENT
 11: 0x009B [0x00] END_REQSTACK()
```

### Event 391

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 63 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      1E F0 FF FF              ....
00A0: 7F 6F 70 29 0B 53 F0 0E  01 06 1D 05 80 23 29 0B  .op).S.......#).
00B0: 53 F0 0E 01 07 29 0B 53  F0 0E 01 01 1D 06 80 23  S....).S.......#
00C0: 29 0B 53 F0 0E 01 08 6E  F8 FF FF 7F 07 80 99 F8  ).S....n........
00D0: FF FF 7F 1D 08 80 23 20  00 21 00                 ......# .!.     
```

#### Opcodes

```
  0: 0x009C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polikal-Ramikal (ID: 17756243/0x010EF053), tag_num=0x06)
  4: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8831*)
    → "...Oh, $6! You have Rhinostery authorization-nation."
  5: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AE [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polikal-Ramikal (ID: 17756243/0x010EF053), tag_num=0x07)
  7: 0x00B5 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polikal-Ramikal (ID: 17756243/0x010EF053), tag_num=0x01)
  8: 0x00BC [0x1D] PRINT_EVENT_MESSAGE(message_id=8832*)
    → "...I heard aboutaru the theory that the withering-dithering of the Star Tree is caused by insects chewing-zewing on the roots."
  9: 0x00BF [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00C0 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polikal-Ramikal (ID: 17756243/0x010EF053), tag_num=0x08)
 11: 0x00C7 [0x6E] EventEntity uses emote 1*
 12: 0x00CE [0x99] Wait for EventEntity animation to complete
 13: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8833*)
    → "We'll leave the extermination-termination of the bugs in your capable hands."
 14: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00D7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x00D9 [0x21] END_EVENT
 17: 0x00DA [0x00] END_REQSTACK()
```
