# 16982267 - Taishu-Yaashu

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 364 bytes                     |
| Total Events     | 15                            |
| References Count | 21                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [2](#event-2)             | 0x0001       |     21 |              5 |
| [3](#event-3)             | 0x0016       |     21 |              5 |
| [65535.1](#event-65535-1) | 0x002B       |     21 |              4 |
| [31](#event-31)           | 0x0040       |     11 |              5 |
| [32](#event-32)           | 0x004B       |     11 |              5 |
| [33](#event-33)           | 0x0056       |     11 |              5 |
| [65535.2](#event-65535-2) | 0x0061       |     11 |              5 |
| [65535.3](#event-65535-3) | 0x006C       |     17 |              4 |
| [686](#event-686)         | 0x007D       |      1 |              1 |
| [65535.4](#event-65535-4) | 0x007E       |     30 |              6 |
| [65535.5](#event-65535-5) | 0x009C       |     14 |              4 |
| [65535.6](#event-65535-6) | 0x00AA       |     14 |              4 |
| [65535.7](#event-65535-7) | 0x00B8       |     14 |              4 |
| [65535.8](#event-65535-8) | 0x00C6       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x5AFC      |       23292 |
|       3 | 0xFFFE80D7  |  4294869207 |
|       4 | 0x0399      |         921 |
|       5 | 0x0C26      |        3110 |
|       6 | 0x1308      |        4872 |
|       7 | 0xFFFFFFDD  |  4294967261 |
|       8 | 0xFFFFE5FE  |  4294960638 |
|       9 | 0xFFFFFB8E  |  4294966158 |
|      10 | 0x0413      |        1043 |
|      11 | 0xFFFF0688  |  4294903432 |
|      12 | 0x137CF     |       79823 |
|      13 | 0x0319      |         793 |
|      14 | 0x0028      |          40 |
|      15 | 0xFFFF06C4  |  4294903492 |
|      16 | 0x129DC     |       76252 |
|      17 | 0xFFFF1355  |  4294906709 |
|      18 | 0x1079F     |       67487 |
|      19 | 0xFFFEF28B  |  4294898315 |
|      20 | 0x10719     |       67353 |

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

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 2F 00 F8 FF FF  7F 92 01 F8 FF FF 7F 94   "./............
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0015 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   22 00  2F 00 F8 FF FF 7F 92 01        "./.......
0020: F8 FF FF 7F 94 01 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x0016 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0018 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x001E [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x0024 [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 21 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   33 01 6C F8 FF             3.l..
0030: FF 7F 00 80 01 80 37 02  80 03 80 04 80 05 80 00  ......7.........
```

#### Opcodes

```
  0: 0x002B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x002D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x0036 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.292*, z=-98.089*, y=0.921*, direction=273.3°*
  3: 0x003F [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 1E F0 FF FF 7F 48 06 80  23 21 00                 .....H..#!.     
```

#### Opcodes

```
  0: 0x0040 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0045 [0x48] [System] [4872*]:
    → "DEBUG: Press a button to continue.\u007F1\u0000\u0007"
  2: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0049 [0x21] END_EVENT
  4: 0x004A [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   1E F0 FF FF 7F             .....
0050: 48 06 80 23 21 00                                 H..#!.          
```

#### Opcodes

```
  0: 0x004B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0050 [0x48] [System] [4872*]:
    → "DEBUG: Press a button to continue.\u007F1\u0000\u0007"
  2: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0054 [0x21] END_EVENT
  4: 0x0055 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   1E F0  FF FF 7F 48 06 80 23 21        .....H..#!
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0056 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005B [0x48] [System] [4872*]:
    → "DEBUG: Press a button to continue.\u007F1\u0000\u0007"
  2: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x005F [0x21] END_EVENT
  4: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    1E F0 FF FF 7F 48 06  80 23 21 00               .....H..#!.    
```

#### Opcodes

```
  0: 0x0061 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0066 [0x48] [System] [4872*]:
    → "DEBUG: Press a button to continue.\u007F1\u0000\u0007"
  2: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x006A [0x21] END_EVENT
  4: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 17 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      33 01 37 07              3.7.
0070: 80 08 80 09 80 0A 80 1E  F6 20 03 01 00           ......... ...   
```

#### Opcodes

```
  0: 0x006C [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x006E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.035*, z=-6.658*, y=-1.138*, direction=91.7°*
  2: 0x0077 [0x1E] EventEntity looks at Tinga-Matonga (ID: 16982262/0x010320F6) and starts talking
  3: 0x007C [0x00] END_REQSTACK()
```

### Event 686

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         00                     .  
```

#### Opcodes

```
  0: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            22 00                ".
0080: 2F 00 F8 FF FF 7F 92 01  F8 FF FF 7F 94 01 F8 FF  /...............
0090: FF 7F 37 0B 80 0C 80 00  80 0D 80 00              ..7.........    
```

#### Opcodes

```
  0: 0x007E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0080 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0086 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x008C [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0092 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-63.864*, z=79.823*, y=0.000*, direction=69.7°*
  5: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      32 0E 80 1F              2...
00A0: 00 0F 80 10 80 00 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x009C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=-63.804*, Z=76.252*, Y=0.000*
  2: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                32 0E 80 1F 00 11            2.....
00B0: 80 12 80 00 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x00AA [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00AD [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.587*, Z=67.487*, Y=0.000*
  2: 0x00B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B8   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          32 0E 80 1F 00 13 80 14          2.......
00C0: 80 00 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x00B8 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00BB [0x1F] MOVE_ENTITY: EventEntity moves to X=-68.981*, Z=67.353*, Y=0.000*
  2: 0x00C3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C6  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   22 01  00                             "..       
```

#### Opcodes

```
  0: 0x00C6 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x00C8 [0x00] END_REQSTACK()
```
