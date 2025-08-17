# 17105326 - Antreneau

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 304 bytes                        |
| Total Events     | 13                               |
| References Count | 20                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [340](#event-340)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      5 |              3 |
| [65535.2](#event-655352) | 0x0007       |     20 |              4 |
| [65535.3](#event-655353) | 0x001B       |     20 |              4 |
| [65535.4](#event-655354) | 0x002F       |     27 |              5 |
| [65535.5](#event-655355) | 0x004A       |     14 |              4 |
| [65535.6](#event-655356) | 0x0058       |      6 |              2 |
| [65535.7](#event-655357) | 0x005E       |     29 |              5 |
| [157](#event-157)        | 0x007B       |      1 |              1 |
| [163](#event-163)        | 0x007C       |      1 |              1 |
| [65535.8](#event-655358) | 0x007D       |     14 |              4 |
| [65535.9](#event-655359) | 0x008B       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D7F      |        7551 |
|       1 | 0x004B      |          75 |
|       2 | 0x1D84      |        7556 |
|       3 | 0x004D      |          77 |
|       4 | 0x1D88      |        7560 |
|       5 | 0xFFFCAA92  |  4294748818 |
|       6 | 0x11971     |       72049 |
|       7 | 0xFFFFEC51  |  4294962257 |
|       8 | 0x0000      |           0 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFCBC0A  |  4294753290 |
|      11 | 0x11049     |       69705 |
|      12 | 0xFFFFF47B  |  4294964347 |
|      13 | 0xFFFCBD06  |  4294753542 |
|      14 | 0x10121     |       65825 |
|      15 | 0x113FE     |       70654 |
|      16 | 0xFFFF8AE0  |  4294937312 |
|      17 | 0x07CF      |        1999 |
|      18 | 0x11E23     |       73251 |
|      19 | 0xFFFF76FF  |  4294932223 |

## String References

- **7551**: Hmmm...? Something's different today. Something smells gooooood!
- **7556**: Me too! Me too!
- **7560**: I love it, I love it! I could eat this every day for the rest of my life!

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

### Event 340

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1D 00 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x0002 [0x1D] PRINT_EVENT_MESSAGE(message_id=7551*)
    → "Hmmm...? Something's different today. Something smells gooooood!"
  1: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      66  01 80 F8 FF FF 7F F8 FF         f........
0010: FF 7F 74 6C 6B 30 1D 02  80 23 00                 ..tlk0...#.     
```

#### Opcodes

```
  0: 0x0007 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  1: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7556*)
    → "Me too! Me too!"
  2: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   66 03 80 F8 FF             f....
0020: FF 7F F8 FF FF 7F 6B 61  6E 30 1D 04 80 23 00     ......kan0...#. 
```

#### Opcodes

```
  0: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "kan0" with entities [EventEntity, EventEntity], work=77*
  1: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=7560*)
    → "I love it, I love it! I could eat this every day for the rest of my life!"
  2: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               4E                 N
0030: 00 F8 FF FF 7F 80 F8 FF  FF 7F 92 01 AE 01 05 01  ................
0040: 37 05 80 06 80 07 80 08  80 00                    7.........      
```

#### Opcodes

```
  0: 0x002F [0x4E] SET_ENTITY_HIDE_FLAG: Show EventEntity
  1: 0x0035 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x003A [0x92] Antreneau (ID: 17105326/0x010501AE)->Render.Flags3 ^= 0x01
  3: 0x0040 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-218.478*, z=72.049*, y=-5.039*, direction=0.0°*
  4: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 09 80 1F 00 0A            2.....
0050: 80 0B 80 0C 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-214.006*, Z=69.705*, Y=-2.949*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0058  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          1E AC 01 05 01 00                ......  
```

#### Opcodes

```
  0: 0x0058 [0x1E] EventEntity looks at Thierride (ID: 17105324/0x010501AC) and starts talking
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 29 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 09                2.
0060: 80 1F 00 0D 80 0E 80 0C  80 1F 01 66 03 80 F8 FF  ...........f....
0070: FF 7F F8 FF FF 7F 73 74  64 30 00                 ......std0.     
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-213.754*, Z=65.825*, Y=-2.949*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=77*
  4: 0x007A [0x00] END_REQSTACK()
```

### Event 157

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   00                         .    
```

#### Opcodes

```
  0: 0x007B [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      00                       .   
```

#### Opcodes

```
  0: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         32 09 80               2..
0080: 1F 00 0F 80 10 80 11 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x007D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0080 [0x1F] MOVE_ENTITY: EventEntity moves to X=70.654*, Z=-29.984*, Y=1.999*
  2: 0x0088 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   32 09 80 1F 00             2....
0090: 12 80 13 80 11 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x008B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=73.251*, Z=-35.073*, Y=1.999*
  2: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0098 [0x00] END_REQSTACK()
```
