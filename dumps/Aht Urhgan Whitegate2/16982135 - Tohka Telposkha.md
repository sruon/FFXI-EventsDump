# 16982135 - Tohka Telposkha

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 312 bytes                      |
| Total Events     | 18                             |
| References Count | 17                             |

## List of Events

| Event ID                    | Entrypoint   |   Size |   Instructions |
|-----------------------------|--------------|--------|----------------|
| [65535](#event-65535)       | 0x0000       |      1 |              1 |
| [65535.1](#event-65535-1)   | 0x0001       |      4 |              2 |
| [65535.2](#event-65535-2)   | 0x0005       |      4 |              2 |
| [65535.3](#event-65535-3)   | 0x0009       |      2 |              2 |
| [5080](#event-5080)         | 0x000B       |      1 |              1 |
| [5081](#event-5081)         | 0x000C       |      1 |              1 |
| [5082](#event-5082)         | 0x000D       |      1 |              1 |
| [5083](#event-5083)         | 0x000E       |      1 |              1 |
| [5084](#event-5084)         | 0x000F       |      1 |              1 |
| [5085](#event-5085)         | 0x0010       |      1 |              1 |
| [65535.4](#event-65535-4)   | 0x0011       |     29 |              7 |
| [65535.5](#event-65535-5)   | 0x002E       |     29 |              7 |
| [65535.6](#event-65535-6)   | 0x004B       |     30 |              8 |
| [65535.7](#event-65535-7)   | 0x0069       |     15 |              5 |
| [65535.8](#event-65535-8)   | 0x0078       |     15 |              5 |
| [65535.9](#event-65535-9)   | 0x0087       |     10 |              2 |
| [65535.10](#event-65535-10) | 0x0091       |     10 |              2 |
| [5086](#event-5086)         | 0x009B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x000D      |          13 |
|       3 | 0xFFF74E8B  |  4294397579 |
|       4 | 0x9E99      |       40601 |
|       5 | 0x07CF      |        1999 |
|       6 | 0xFFF74843  |  4294395971 |
|       7 | 0x92C4      |       37572 |
|       8 | 0x0028      |          40 |
|       9 | 0xFFF75025  |  4294397989 |
|      10 | 0x87F8      |       34808 |
|      11 | 0xFFF7681F  |  4294404127 |
|      12 | 0x9BD1      |       39889 |
|      13 | 0xFFF76051  |  4294402129 |
|      14 | 0x8D30      |       36144 |
|      15 | 0x003C      |          60 |
|      16 | 0x0080      |         128 |

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
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    95 00 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 1*)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                95 01 80  00                            ....       
```

#### Opcodes

```
  0: 0x0005 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             96 00                          ..     
```

#### Opcodes

```
  0: 0x0009 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 5080

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

### Event 5081

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

### Event 5082

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         00                     .  
```

#### Opcodes

```
  0: 0x000D [0x00] END_REQSTACK()
```

### Event 5083

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            00                   . 
```

#### Opcodes

```
  0: 0x000E [0x00] END_REQSTACK()
```

### Event 5084

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 5085

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    7B 77 20 03 01 32 02  80 1F 00 03 80 04 80 05   {w ..2.........
0020: 80 1F 01 6F 4A 77 20 03  01 C6 21 03 01 00        ...oJw ...!...  
```

#### Opcodes

```
  0: 0x0011 [0x7B] Tohka Telposkha (ID: 16982135/0x01032077) stops talking
  1: 0x0016 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=-569.717*, Z=40.601*, Y=1.999*
  3: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0024 [0x4A] Tohka Telposkha (ID: 16982135/0x01032077) looks at Rongelouts (ID: 16982470/0x010321C6)
  6: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            7B 77                {w
0030: 20 03 01 32 02 80 1F 00  06 80 07 80 05 80 1F 01   ..2............
0040: 6F 4A 77 20 03 01 C6 21  03 01 00                 oJw ...!...     
```

#### Opcodes

```
  0: 0x002E [0x7B] Tohka Telposkha (ID: 16982135/0x01032077) stops talking
  1: 0x0033 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=-571.325*, Z=37.572*, Y=1.999*
  3: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0041 [0x4A] Tohka Telposkha (ID: 16982135/0x01032077) looks at Rongelouts (ID: 16982470/0x010321C6)
  6: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   32 08 80 1F 00             2....
0050: 09 80 0A 80 05 80 1F 01  6F 4A 76 20 03 01 CC 21  ........oJv ...!
0060: 03 01 6F 76 76 20 03 01  00                       ..ovv ...       
```

#### Opcodes

```
  0: 0x004B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-569.307*, Z=34.808*, Y=1.999*
  2: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0058 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0059 [0x4A] Kubhe Ijyuhla (ID: 16982134/0x01032076) looks at Silver Kettle (ID: 16982476/0x010321CC)
  5: 0x0062 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0063 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Kubhe Ijyuhla (ID: 16982134/0x01032076) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 02 80 1F 00 0B 80           2......
0070: 0C 80 05 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-563.169*, Z=39.889*, Y=1.999*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          32 02 80 1F 00 0D 80 0E          2.......
0080: 80 05 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0078 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=-565.167*, Z=36.144*, Y=1.999*
  2: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0085 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      6C  F8 FF FF 7F 01 80 0F 80         l........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    6C F8 FF FF 7F 10 80  0F 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0091 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=60*)
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 5086

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   00                         .    
```

#### Opcodes

```
  0: 0x009B [0x00] END_REQSTACK()
```
