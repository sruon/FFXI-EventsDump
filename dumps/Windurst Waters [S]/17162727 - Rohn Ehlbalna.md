# 17162727 - Rohn Ehlbalna

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 360 bytes                    |
| Total Events     | 15                           |
| References Count | 20                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [114](#event-114)        | 0x0001       |      1 |              1 |
| [115](#event-115)        | 0x0002       |     18 |              6 |
| [111](#event-111)        | 0x0014       |      5 |              2 |
| [108](#event-108)        | 0x0019       |      5 |              2 |
| [65535.1](#event-655351) | 0x001E       |     30 |              7 |
| [65535.2](#event-655352) | 0x003C       |     15 |              5 |
| [440](#event-440)        | 0x004B       |     60 |             10 |
| [65535.3](#event-655353) | 0x0087       |     20 |              6 |
| [128](#event-128)        | 0x009B       |      7 |              2 |
| [129](#event-129)        | 0x00A2       |      7 |              2 |
| [133](#event-133)        | 0x00A9       |      7 |              2 |
| [134](#event-134)        | 0x00B0       |      7 |              2 |
| [65535.4](#event-655354) | 0x00B7       |      5 |              2 |
| [32](#event-32)          | 0x00BC       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2CAD      |       11437 |
|       2 | 0x005D      |          93 |
|       3 | 0x0050      |          80 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF5BCF  |  4294925263 |
|       6 | 0xFFFD7F30  |  4294803248 |
|       7 | 0xFFFFFB8F  |  4294966159 |
|       8 | 0xFFFF5938  |  4294924600 |
|       9 | 0xFFFD6822  |  4294797346 |
|      10 | 0xFFFFFB1F  |  4294966047 |
|      11 | 0x003B      |          59 |
|      12 | 0x2AD5      |       10965 |
|      13 | 0x2AD6      |       10966 |
|      14 | 0xFFFF56CF  |  4294923983 |
|      15 | 0xFFFD8207  |  4294803975 |
|      16 | 0xFFFF5C7A  |  4294925434 |
|      17 | 0xFFFD853E  |  4294804798 |
|      18 | 0xFFFFFB94  |  4294966164 |
|      19 | 0x02BB      |         699 |

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

### Event 114

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

### Event 115

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 1C  00 80 2B E7 E1 05 01 01    ........+.....
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x1C] WAIT(30* ticks)
  2: 0x000A [0x2B] Rohn Ehlbalna (ID: 17162727/0x0105E1E7) [11437*]:
    → "Please, tell Kocco what a cruel and difficult place the world can be. I'd be most apprrreciative."
  3: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0012 [0x21] END_EVENT
  5: 0x0013 [0x00] END_REQSTACK()
```

### Event 111

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             B6 0F 02 80  00                           .....       
```

#### Opcodes

```
  0: 0x0014 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=93*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             B6 0F 03 80 00                 .....  
```

#### Opcodes

```
  0: 0x0019 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=80*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 30 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            79 00                y.
0020: E7 E1 05 01 00 E2 05 01  32 04 80 1F 00 05 80 06  ........2.......
0030: 80 07 80 1F 01 6F 1E 00  E2 05 01 00              .....o......    
```

#### Opcodes

```
  0: 0x001E [0x79] Rohn Ehlbalna (ID: 17162727/0x0105E1E7) looks at Kocco Ehllek (ID: 17162752/0x0105E200) (Basic look)
  1: 0x0028 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.033*, Z=-164.048*, Y=-1.137*
  3: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0036 [0x1E] EventEntity looks at Kocco Ehllek (ID: 17162752/0x0105E200) and starts talking
  6: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 04 80 1F              2...
0040: 00 08 80 09 80 0A 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.696*, Z=-169.950*, Y=-1.249*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004A [0x00] END_REQSTACK()
```

### Event 440

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   4A F8 FF FF 7F             J....
0050: F0 FF FF 7F 1C 00 80 66  0B 80 F8 FF FF 7F F8 FF  .......f........
0060: FF 7F 74 6C 6B 30 2B F8  FF FF 7F 0C 80 23 2B F8  ..tlk0+......#+.
0070: FF FF 7F 0D 80 23 66 0B  80 F8 FF FF 7F F8 FF FF  .....#f.........
0080: 7F 74 6C 6B 31 21 00                              .tlk1!.         
```

#### Opcodes

```
  0: 0x004B [0x4A] EventEntity looks at LocalPlayer
  1: 0x0054 [0x1C] WAIT(30* ticks)
  2: 0x0057 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x0066 [0x2B] EventEntity [10965*]:
    → "Yes, I'm a Mithra Mercenary. Do you know of my unit, adventurer? The Anacondas. Led by the grrreat Perih Vashai."
  4: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x006E [0x2B] EventEntity [10966*]:
    → "She is a master of the bow. And not only strong, but smarrrt as a whip to boot. There aren't many leaders these days so trusted by their troops as she."
  6: 0x0075 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0076 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  8: 0x0085 [0x21] END_EVENT
  9: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      32  04 80 1F 00 0E 80 0F 80         2........
0090: 0A 80 1F 01 6F 1E 00 E2  05 01 00                 ....o......     
```

#### Opcodes

```
  0: 0x0087 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008A [0x1F] MOVE_ENTITY: EventEntity moves to X=-43.313*, Z=-163.321*, Y=-1.249*
  2: 0x0092 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0094 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0095 [0x1E] EventEntity looks at Kocco Ehllek (ID: 17162752/0x0105E200) and starts talking
  5: 0x009A [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   92 01 F8 FF FF             .....
00A0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x009B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A1 [0x00] END_REQSTACK()
```

### Event 129

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x00A2 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 133

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x00A9 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AF [0x00] END_REQSTACK()
```

### Event 134

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B0  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00B0 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B7  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      B6  0F 02 80 00                     .....    
```

#### Opcodes

```
  0: 0x00B7 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=93*)
  1: 0x00BB [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      BA F8 FF FF              ....
00C0: 7F 10 80 11 80 12 80 13  80 00                    ..........      
```

#### Opcodes

```
  0: 0x00BC [0xBA] SET_ENTITY_POSITION(entity_id=EventEntity, pos_x=-41.862*, pos_z=-162.498*, pos_y=-1.132*, direction=61.4°*)
  1: 0x00C9 [0x00] END_REQSTACK()
```
