# 17142516 - Childerich

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 272 bytes             |
| Total Events     | 10                    |
| References Count | 14                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10](#event-10)          | 0x0001       |     29 |              7 |
| [1](#event-1)            | 0x001E       |      1 |              1 |
| [2](#event-2)            | 0x001F       |     29 |              7 |
| [4](#event-4)            | 0x003C       |      1 |              1 |
| [5](#event-5)            | 0x003D       |     29 |              7 |
| [6](#event-6)            | 0x005A       |      1 |              1 |
| [65535.1](#event-655351) | 0x005B       |     14 |              4 |
| [65535.2](#event-655352) | 0x0069       |     40 |              8 |
| [7](#event-7)            | 0x0091       |     14 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0009      |           9 |
|       2 | 0x1E40      |        7744 |
|       3 | 0x1E3F      |        7743 |
|       4 | 0x1E4E      |        7758 |
|       5 | 0x000D      |          13 |
|       6 | 0xFFFB433D  |  4294656829 |
|       7 | 0xFFF8293F  |  4294453567 |
|       8 | 0x3F79      |       16249 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFB31FB  |  4294652411 |
|      11 | 0xFFF82043  |  4294451267 |
|      12 | 0x3EB1      |       16049 |
|      13 | 0x1E69      |        7785 |

## String References

- **7743**: Romualdo's father died on this mountain years ago. And the deceased don't make a habit of chatting to the living.
- **7744**: What are you doing way out here? This is no place for civilians.
- **7758**: I think it's time I put in for a transfer to a new outpost...
- **7785**: This is it. The madness of the mountains has finally sunk into my soul...

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

### Event 10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 21 00        ....tlk0...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7744*)
    → "What are you doing way out here? This is no place for civilians."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x21] END_EVENT
  6: 0x001D [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: F0 FF FF 7F 1C 00 80 66  01 80 F8 FF FF 7F F8 FF  .......f........
0030: FF 7F 74 6C 6B 30 1D 03  80 23 21 00              ..tlk0...#!.    
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0024 [0x1C] WAIT(30* ticks)
  2: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  3: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=7743*)
    → "Romualdo's father died on this mountain years ago. And the deceased don't make a habit of chatting to the living."
  4: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003A [0x21] END_EVENT
  6: 0x003B [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1E F0 FF               ...
0040: FF 7F 1C 00 80 66 01 80  F8 FF FF 7F F8 FF FF 7F  .....f..........
0050: 74 6C 6B 30 1D 04 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x003D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0042 [0x1C] WAIT(30* ticks)
  2: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  3: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7758*)
    → "I think it's time I put in for a transfer to a new outpost..."
  4: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0058 [0x21] END_EVENT
  6: 0x0059 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                00                           .     
```

#### Opcodes

```
  0: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 05 80 1F 00             2....
0060: 06 80 07 80 08 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=-310.467*, Z=-513.729*, Y=16.249*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 40 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 09 80 1F 00 0A 80           2......
0070: 0B 80 0C 80 1F 01 1E F5  92 05 01 4A F0 FF FF 7F  ...........J....
0080: F4 92 05 01 4A F5 92 05  01 F4 92 05 01 1C 00 80  ....J...........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-314.885*, Z=-516.029*, Y=16.049*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x1E] EventEntity looks at Bhoratz (ID: 17142517/0x010592F5) and starts talking
  4: 0x007B [0x4A] LocalPlayer looks at Childerich (ID: 17142516/0x010592F4)
  5: 0x0084 [0x4A] Bhoratz (ID: 17142517/0x010592F5) looks at Childerich (ID: 17142516/0x010592F4)
  6: 0x008D [0x1C] WAIT(30* ticks)
  7: 0x0090 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    1E F0 FF FF 7F 1C 00  80 1D 0D 80 23 21 00      ...........#!. 
```

#### Opcodes

```
  0: 0x0091 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0096 [0x1C] WAIT(30* ticks)
  2: 0x0099 [0x1D] PRINT_EVENT_MESSAGE(message_id=7785*)
    → "This is it. The madness of the mountains has finally sunk into my soul..."
  3: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x009D [0x21] END_EVENT
  5: 0x009E [0x00] END_REQSTACK()
```
