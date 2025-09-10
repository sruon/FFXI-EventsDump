# 16994430 - Kakkaroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 296 bytes        |
| Total Events     | 11               |
| References Count | 23               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [308](#event-308)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              6 |
| [65535.2](#event-655352) | 0x001A       |     24 |              6 |
| [65535.3](#event-655353) | 0x0032       |     25 |              7 |
| [65535.4](#event-655354) | 0x004B       |     15 |              5 |
| [311](#event-311)        | 0x005A       |      1 |              1 |
| [312](#event-312)        | 0x005B       |      1 |              1 |
| [65535.5](#event-655355) | 0x005C       |     15 |              5 |
| [313](#event-313)        | 0x006B       |     19 |              9 |
| [314](#event-314)        | 0x007E       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x425B      |       16987 |
|       2 | 0xFFFF974B  |  4294940491 |
|       3 | 0x0000      |           0 |
|       4 | 0x5AA2      |       23202 |
|       5 | 0xFFFF86A0  |  4294936224 |
|       6 | 0x472D      |       18221 |
|       7 | 0xFFFF7AF2  |  4294933234 |
|       8 | 0x06D9      |        1753 |
|       9 | 0x000D      |          13 |
|      10 | 0x4C16      |       19478 |
|      11 | 0xFFFF91AF  |  4294939055 |
|      12 | 0x46FE      |       18174 |
|      13 | 0xFFFF9518  |  4294939928 |
|      14 | 0x4103      |       16643 |
|      15 | 0xFFFF9795  |  4294940565 |
|      16 | 0x0C0A      |        3082 |
|      17 | 0x532A      |       21290 |
|      18 | 0x2CCA      |       11466 |
|      19 | 0x2CCB      |       11467 |
|      20 | 0x2CCF      |       11471 |
|      21 | 0x2D7D      |       11645 |
|      22 | 0x2D7E      |       11646 |

## String References

- **11466**: Kakka 'fraid tooo come out from places of hiding.
- **11467**: Kakka want tooo beee with Nadeee. Nadeee understand heart of Kakka.
- **11471**: But Nadeee go away. Nadeee leeeve Kakka alone behind cart of carrying...
- **11645**: Everybodeee have, but Kakkaroon no have! Sisiroon is everybodeee, but Kakkaroon is nobodeee!
- **11646**: <Sigh>...

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

### Event 308

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 4A F0 FF FF 7F 7E 50 03  01 00                    J....~P...      
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=16.987*, Z=-26.805*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x4A] LocalPlayer looks at Kakkaroon (ID: 16994430/0x0103507E)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 00 80 1F 00 04            2.....
0020: 80 05 80 03 80 1F 01 6F  37 06 80 07 80 03 80 08  .......o7.......
0030: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=23.202*, Z=-31.072*, Y=0.000*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0028 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.221*, z=-34.062*, y=0.000*, direction=154.1°*
  5: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       32 09 80 1F 00 0A  80 0B 80 03 80 1F 01 1F    2.............
0040: 00 0C 80 0D 80 03 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x0032 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0035 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.478*, Z=-28.241*, Y=0.000*
  2: 0x003D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=18.174*, Z=-27.368*, Y=0.000*
  4: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   32 09 80 1F 00             2....
0050: 0E 80 0F 80 03 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x004B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=16.643*, Z=-26.731*, Y=0.000*
  2: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0058 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0059 [0x00] END_REQSTACK()
```

### Event 311

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

### Event 312

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 00 80 1F              2...
0060: 00 10 80 11 80 03 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=3.082*, Z=21.290*, Y=0.000*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006A [0x00] END_REQSTACK()
```

### Event 313

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   1E F0 FF FF 7F             .....
0070: 1D 12 80 23 1D 13 80 23  1D 14 80 23 21 00        ...#...#...#!.  
```

#### Opcodes

```
  0: 0x006B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=11466*)
    → "Kakka 'fraid tooo come out from places of hiding."
  2: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=11467*)
    → "Kakka want tooo beee with Nadeee. Nadeee understand heart of Kakka."
  4: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0078 [0x1D] PRINT_EVENT_MESSAGE(message_id=11471*)
    → "But Nadeee go away. Nadeee leeeve Kakka alone behind cart of carrying..."
  6: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x007C [0x21] END_EVENT
  8: 0x007D [0x00] END_REQSTACK()
```

### Event 314

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            1E F0                ..
0080: FF FF 7F 1D 15 80 23 1D  16 80 23 21 00           ......#...#!.   
```

#### Opcodes

```
  0: 0x007E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0083 [0x1D] PRINT_EVENT_MESSAGE(message_id=11645*)
    → "Everybodeee have, but Kakkaroon no have! Sisiroon is everybodeee, but Kakkaroon is nobodeee!"
  2: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=11646*)
    → "<Sigh>..."
  4: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x008B [0x21] END_EVENT
  6: 0x008C [0x00] END_REQSTACK()
```
