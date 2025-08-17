# 16830630 - Shikaree Z

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Mine Shaft #2716 (ID: 13) |
| Block Size       | 436 bytes                 |
| Total Events     | 16                        |
| References Count | 38                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [0](#event-0)              | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     18 |              4 |
| [65535.2](#event-655352)   | 0x0014       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001E       |      9 |              3 |
| [65535.4](#event-655354)   | 0x0027       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0030       |     10 |              2 |
| [65535.6](#event-655356)   | 0x003A       |     10 |              2 |
| [4](#event-4)              | 0x0044       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0045       |     10 |              2 |
| [65535.8](#event-655358)   | 0x004F       |     15 |              5 |
| [65535.9](#event-655359)   | 0x005E       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0068       |     15 |              5 |
| [65535.11](#event-6553511) | 0x0077       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0081       |     29 |              9 |
| [65535.13](#event-6553513) | 0x009E       |     45 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFF90055  |  4294508629 |
|       4 | 0xFFFFA0F7  |  4294942967 |
|       5 | 0x1D4BF     |      119999 |
|       6 | 0x0C03      |        3075 |
|       7 | 0x0028      |          40 |
|       8 | 0xFFF90284  |  4294509188 |
|       9 | 0xFFFFEAB7  |  4294961847 |
|      10 | 0xFFF9044D  |  4294509645 |
|      11 | 0x1EC6      |        7878 |
|      12 | 0x1DC80     |      121984 |
|      13 | 0x0B26      |        2854 |
|      14 | 0x0026      |          38 |
|      15 | 0xFFF906B2  |  4294510258 |
|      16 | 0x376D      |       14189 |
|      17 | 0x1DD5B     |      122203 |
|      18 | 0xFFF8AF85  |  4294487941 |
|      19 | 0x4A08      |       18952 |
|      20 | 0x1D55A     |      120154 |
|      21 | 0x0020      |          32 |
|      22 | 0x000D      |          13 |
|      23 | 0xFFF8C774  |  4294494068 |
|      24 | 0x4560      |       17760 |
|      25 | 0x1DC88     |      121992 |
|      26 | 0xFFF8D2B5  |  4294496949 |
|      27 | 0x4480      |       17536 |
|      28 | 0xFFF8E525  |  4294501669 |
|      29 | 0x2DD8      |       11736 |
|      30 | 0x1DC8F     |      121999 |
|      31 | 0xFFF8EE84  |  4294504068 |
|      32 | 0x1D29      |        7465 |
|      33 | 0xFFF8F559  |  4294505817 |
|      34 | 0xFFFFFF32  |  4294967090 |
|      35 | 0x1D462     |      119906 |
|      36 | 0xFFF8F956  |  4294506838 |
|      37 | 0xFFFFD7B9  |  4294956985 |

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

### Event 0

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
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                37 03 80  04 80 05 80 06 80 00          7......... 
```

#### Opcodes

```
  0: 0x0045 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-458.667*, z=-24.329*, y=119.999*, direction=270.3°*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 07 80 1F 00 08 80 09 80  05 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-458.108*, Z=-5.449*, Y=119.999*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            37 0A                7.
0060: 80 0B 80 0C 80 0D 80 00                           ........        
```

#### Opcodes

```
  0: 0x005E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-457.651*, z=7.878*, y=121.984*, direction=250.8°*
  1: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          32 0E 80 1F 00 0F 80 10          2.......
0070: 80 11 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0068 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x006B [0x1F] MOVE_ENTITY: EventEntity moves to X=-457.038*, Z=14.189*, Y=122.203*
  2: 0x0073 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0075 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      37  12 80 13 80 14 80 15 80         7........
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0077 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-479.355*, z=18.952*, y=120.154*, direction=2.8°*
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    33 01 32 16 80 5A 00  17 80 18 80 19 80 5A 01   3.2..Z.......Z.
0090: 1F 00 1A 80 1B 80 19 80  1F 01 6F 33 00 00        ..........o3..  
```

#### Opcodes

```
  0: 0x0081 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0083 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0086 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-473.228*, Z=17.760*, Y=121.992*
  3: 0x008E [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  4: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=-470.347*, Z=17.536*, Y=121.992*
  5: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x009A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x009B [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  8: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            32 07                2.
00A0: 80 1F 00 1C 80 1D 80 1E  80 1F 01 1F 00 1F 80 20  ............... 
00B0: 80 1E 80 1F 01 1F 00 21  80 22 80 23 80 1F 01 1F  .......!.".#....
00C0: 00 24 80 25 80 05 80 1F  01 6F 00                 .$.%.....o.     
```

#### Opcodes

```
  0: 0x009E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-465.627*, Z=11.736*, Y=121.999*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x1F] MOVE_ENTITY: EventEntity moves to X=-463.228*, Z=7.465*, Y=121.999*
  4: 0x00B3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-461.479*, Z=-0.206*, Y=119.906*
  6: 0x00BD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=-460.458*, Z=-10.311*, Y=119.999*
  8: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00C9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x00CA [0x00] END_REQSTACK()
```
