# 17171238 - Nzha Abaleenah

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 344 bytes                       |
| Total Events     | 14                              |
| References Count | 20                              |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [113](#event-113)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |      5 |              2 |
| [65535.2](#event-655352)   | 0x0007       |      5 |              2 |
| [65535.3](#event-655353)   | 0x000C       |      5 |              2 |
| [65535.4](#event-655354)   | 0x0011       |     21 |              2 |
| [65535.5](#event-655355)   | 0x0026       |     21 |              2 |
| [65535.6](#event-655356)   | 0x003B       |      5 |              2 |
| [65535.7](#event-655357)   | 0x0040       |     25 |              3 |
| [65535.8](#event-655358)   | 0x0059       |     25 |              3 |
| [65535.9](#event-655359)   | 0x0072       |     25 |              3 |
| [65535.10](#event-6553510) | 0x008B       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0099       |     14 |              4 |
| [65535.12](#event-6553512) | 0x00A7       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x02F3      |         755 |
|       1 | 0x043C      |        1084 |
|       2 | 0x08C3      |        2243 |
|       3 | 0x0007      |           7 |
|       4 | 0x0003      |           3 |
|       5 | 0x0000      |           0 |
|       6 | 0x005E      |          94 |
|       7 | 0x000E      |          14 |
|       8 | 0x006E      |         110 |
|       9 | 0x0317      |         791 |
|      10 | 0x000D      |          13 |
|      11 | 0xFFFFCF94  |  4294954900 |
|      12 | 0xFFFECAF5  |  4294888181 |
|      13 | 0xFFFEF661  |  4294899297 |
|      14 | 0xFFFFCFBC  |  4294954940 |
|      15 | 0xFFFEC473  |  4294886515 |
|      16 | 0xFFF8DEBA  |  4294500026 |
|      17 | 0xC0BF      |       49343 |
|      18 | 0xFFFF8E45  |  4294938181 |
|      19 | 0x001E      |          30 |

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

### Event 113

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
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 00 00 80 00                                .....         
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=755*)
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      B6  00 01 80 00                     .....    
```

#### Opcodes

```
  0: 0x0007 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1084*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      B6 00 02 80              ....
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2243*)
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    B6 0B 03 80 04 80 05  80 06 80 06 80 07 80 07   ...............
0020: 80 05 80 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0011 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=3*, head=0*, body=94*, hands=94*, legs=14*, feet=14*, main=0*, sub=0*)
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   B6 0B  03 80 04 80 05 80 06 80        ..........
0030: 06 80 07 80 07 80 08 80  05 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0026 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=3*, head=0*, body=94*, hands=94*, legs=14*, feet=14*, main=110*, sub=0*)
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   B6 00 09 80 00             .....
```

#### Opcodes

```
  0: 0x003B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=791*)
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: B4 00 00 00 3F 3F 3F 00  00 00 00 00 00 00 00 00  ....???.........
0050: 00 00 00 00 B5 00 00 00  00                       .........       
```

#### Opcodes

```
  0: 0x0040 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x0054 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             B4 00 00 00 52 6F 62           ....Rob
0060: 65 6C 2D 41 6B 62 65 6C  00 00 00 00 00 B5 00 00  el-Akbel........
0070: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x0059 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="Robel-Akbel")
  1: 0x006D [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       B4 00 00 00 30 32  00 00 00 00 00 00 00 00    ....02........
0080: 00 00 00 00 00 00 B5 00  00 00 00                 ...........     
```

#### Opcodes

```
  0: 0x0072 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="02")
  1: 0x0086 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   32 0A 80 1F 00             2....
0090: 0B 80 0C 80 0D 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x008B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.396*, Z=-79.115*, Y=-67.999*
  2: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             32 0A 80 1F 00 0E 80           2......
00A0: 0F 80 0D 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0099 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=-12.356*, Z=-80.781*, Y=-67.999*
  2: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      32  0A 80 5A 00 10 80 11 80         2..Z.....
00B0: 12 80 5A 01 1E F0 FF FF  7F 1C 13 80 00           ..Z..........   
```

#### Opcodes

```
  0: 0x00A7 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00AA [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-467.270*, Z=49.343*, Y=-29.115*
  2: 0x00B2 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00B9 [0x1C] WAIT(30* ticks)
  5: 0x00BC [0x00] END_REQSTACK()
```
