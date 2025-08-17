# 17162752 - Kocco Ehllek

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 292 bytes                    |
| Total Events     | 14                           |
| References Count | 14                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      5 |              2 |
| [108](#event-108)        | 0x0006       |      5 |              2 |
| [109](#event-109)        | 0x000B       |      1 |              1 |
| [110](#event-110)        | 0x000C       |      1 |              1 |
| [111](#event-111)        | 0x000D       |      5 |              2 |
| [140](#event-140)        | 0x0012       |     18 |              6 |
| [113](#event-113)        | 0x0024       |     25 |              7 |
| [116](#event-116)        | 0x003D       |     25 |              7 |
| [112](#event-112)        | 0x0056       |     25 |              7 |
| [65535.2](#event-655352) | 0x006F       |      4 |              2 |
| [65535.3](#event-655353) | 0x0073       |     12 |              3 |
| [220](#event-220)        | 0x007F       |     33 |              9 |
| [32](#event-32)          | 0x00A0       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x005D      |          93 |
|       1 | 0x0050      |          80 |
|       2 | 0x001E      |          30 |
|       3 | 0x2CA3      |       11427 |
|       4 | 0x2CBB      |       11451 |
|       5 | 0x2CC4      |       11460 |
|       6 | 0x2CDF      |       11487 |
|       7 | 0x0000      |           0 |
|       8 | 0xFFFF5E67  |  4294925927 |
|       9 | 0xFFFD853D  |  4294804797 |
|      10 | 0xFFFFFB8E  |  4294966158 |
|      11 | 0x00B4      |         180 |
|      12 | 0x2AEC      |       10988 |
|      13 | 0x2AED      |       10989 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 0F 00 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=93*)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   B6 0F  01 80 00                       .....     
```

#### Opcodes

```
  0: 0x0006 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=80*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   00                         .    
```

#### Opcodes

```
  0: 0x000B [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 111

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         B6 0F 00               ...
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=93*)
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 140

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       1E F0 FF FF 7F 1C  02 80 2B 00 E2 05 01 03    ........+.....
0020: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0017 [0x1C] WAIT(30* ticks)
  2: 0x001A [0x2B] Kocco Ehllek (ID: 17162752/0x0105E200) [11427*]:
    → "Mama... Meeeooow..."
  3: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0022 [0x21] END_EVENT
  5: 0x0023 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1E F0 FF FF  7F 29 10 F0 FF FF 7F 0B      .....)......
0030: 1C 02 80 2B 00 E2 05 01  04 80 23 21 00           ...+......#!.   
```

#### Opcodes

```
  0: 0x0024 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0029 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0B)
  2: 0x0030 [0x1C] WAIT(30* ticks)
  3: 0x0033 [0x2B] Kocco Ehllek (ID: 17162752/0x0105E200) [11451*]:
    → "Oh pleeease, brrring me a shiny blue stone from Vunkerrrl Inlet!"
  4: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003B [0x21] END_EVENT
  6: 0x003C [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1E F0 FF               ...
0040: FF 7F 29 10 F0 FF FF 7F  0B 1C 02 80 2B 00 E2 05  ..).........+...
0050: 01 05 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x003D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0042 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0B)
  2: 0x0049 [0x1C] WAIT(30* ticks)
  3: 0x004C [0x2B] Kocco Ehllek (ID: 17162752/0x0105E200) [11460*]:
    → "Nehehe! It should be finished by tomorrow! Meow!"
  4: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0054 [0x21] END_EVENT
  6: 0x0055 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   1E F0  FF FF 7F 29 10 F0 FF FF        .....)....
0060: 7F 0B 1C 02 80 2B 00 E2  05 01 06 80 23 21 00     .....+......#!. 
```

#### Opcodes

```
  0: 0x0056 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005B [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0B)
  2: 0x0062 [0x1C] WAIT(30* ticks)
  3: 0x0065 [0x2B] Kocco Ehllek (ID: 17162752/0x0105E200) [11487*]:
    → "Thank you so much for brrringing me that shiny stone! I wonder if it is keeping Mama safe..."
  4: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x006D [0x21] END_EVENT
  6: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006F  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               39                 9
0070: 07 80 00                                          ...             
```

#### Opcodes

```
  0: 0x006F [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          33 01 37 08 80  09 80 0A 80 0B 80 00        3.7......... 
```

#### Opcodes

```
  0: 0x0073 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0075 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-41.369*, z=-162.499*, y=-1.138*, direction=15.8°*
  2: 0x007E [0x00] END_REQSTACK()
```

### Event 220

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               1E                 .
0080: F0 FF FF 7F 29 10 F0 FF  FF 7F 0B 1C 02 80 2B 00  ....).........+.
0090: E2 05 01 0C 80 23 2B 00  E2 05 01 0D 80 23 21 00  .....#+......#!.
```

#### Opcodes

```
  0: 0x007F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0084 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0B)
  2: 0x008B [0x1C] WAIT(30* ticks)
  3: 0x008E [0x2B] Kocco Ehllek (ID: 17162752/0x0105E200) [10988*]:
    → "Meeeooow... They say it's dangerrrous here, but I can't leave without my mama! Have you seen her anywhere, [mister/lady]?"
  4: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0096 [0x2B] Kocco Ehllek (ID: 17162752/0x0105E200) [10989*]:
    → "Mama is big and strrrong, and loves me more than anyone in the whole wide world. I know she'll come back soon!"
  6: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009E [0x21] END_EVENT
  8: 0x009F [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A0  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A0 [0x00] END_REQSTACK()
```
