# 16912925 - Nagmolada

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 424 bytes         |
| Total Events     | 21                |
| References Count | 29                |

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
| [1](#event-1)              | 0x0044       |      1 |              1 |
| [2](#event-2)              | 0x0045       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0046       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0050       |     10 |              2 |
| [65535.9](#event-655359)   | 0x005A       |     12 |              3 |
| [65535.10](#event-6553510) | 0x0066       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0070       |     15 |              5 |
| [65535.12](#event-6553512) | 0x007F       |     15 |              5 |
| [65535.13](#event-6553513) | 0x008E       |     10 |              2 |
| [65535.14](#event-6553514) | 0x0098       |     27 |              7 |
| [65535.15](#event-6553515) | 0x00B3       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00C1       |     14 |              2 |
| [7](#event-7)              | 0x00CF       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x642E4     |      410340 |
|       4 | 0xFFF912F7  |  4294513399 |
|       5 | 0xFFFFB606  |  4294948358 |
|       6 | 0x0800      |        2048 |
|       7 | 0x640C0     |      409792 |
|       8 | 0xFFF91316  |  4294513430 |
|       9 | 0xFFFFB654  |  4294948436 |
|      10 | 0x623C8     |      402376 |
|      11 | 0xFFF912B8  |  4294513336 |
|      12 | 0xFFFFB565  |  4294948197 |
|      13 | 0xFFF9836B  |  4294542187 |
|      14 | 0xFFF7E181  |  4294435201 |
|      15 | 0x00A1      |         161 |
|      16 | 0x000D      |          13 |
|      17 | 0xFFF99E80  |  4294549120 |
|      18 | 0xFFF7DD13  |  4294434067 |
|      19 | 0xFFF9BA56  |  4294556246 |
|      20 | 0xFFF7DF52  |  4294434642 |
|      21 | 0xFFF9AF41  |  4294553409 |
|      22 | 0xFFF804C0  |  4294444224 |
|      23 | 0x0DA2      |        3490 |
|      24 | 0xFFF9C775  |  4294559605 |
|      25 | 0xFFF7F75E  |  4294440798 |
|      26 | 0x0022      |          34 |
|      27 | 0xFFFA05C5  |  4294575557 |
|      28 | 0xFFF7DBF4  |  4294433780 |

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

### Event 1

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

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 03  80 04 80 05 80 06 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=410.340*, z=-453.897*, y=-18.938*, direction=180.0°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 37 07 80 08 80 09 80 06  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0050 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=409.792*, z=-453.866*, y=-18.860*, direction=180.0°*
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                A4 01 37 0A 80 0B            ..7...
0060: 80 0C 80 06 80 00                                 ......          
```

#### Opcodes

```
  0: 0x005A [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x005C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=402.376*, z=-453.960*, y=-19.099*, direction=180.0°*
  2: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   37 0D  80 0E 80 00 80 0F 80 00        7.........
```

#### Opcodes

```
  0: 0x0066 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-425.109*, z=-532.095*, y=0.000*, direction=14.1°*
  1: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 32 10 80 1F 00 11 80 12  80 00 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0070 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=-418.176*, Z=-533.229*, Y=0.000*
  2: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               32                 2
0080: 10 80 1F 00 13 80 14 80  00 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x007F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0082 [0x1F] MOVE_ENTITY: EventEntity moves to X=-411.050*, Z=-532.654*, Y=0.000*
  2: 0x008A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008D [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            37 15                7.
0090: 80 16 80 00 80 17 80 00                           ........        
```

#### Opcodes

```
  0: 0x008E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-413.887*, z=-523.072*, y=0.000*, direction=306.7°*
  1: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          37 18 80 19 80 00 80 1A          7.......
00A0: 80 1C 01 80 32 10 80 1F  00 1B 80 1C 80 00 80 1F  ....2...........
00B0: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0098 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-407.691*, z=-526.498*, y=0.000*, direction=3.0°*
  1: 0x00A1 [0x1C] WAIT(1* ticks)
  2: 0x00A4 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x00A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-391.739*, Z=-533.516*, Y=0.000*
  4: 0x00AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00B2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          2C 1D 12 02 01  1D 12 02 01 77 6F 6E 32     ,........won2
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B3 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "won2" with entities [Nag'molada (ID: 16912925/0x0102121D), Nag'molada (ID: 16912925/0x0102121D)]
  1: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    2C 1D 12 02 01 1D 12  02 01 77 6F 66 32 00      ,........wof2. 
```

#### Opcodes

```
  0: 0x00C1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "wof2" with entities [Nag'molada (ID: 16912925/0x0102121D), Nag'molada (ID: 16912925/0x0102121D)]
  1: 0x00CE [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               00                 .
```

#### Opcodes

```
  0: 0x00CF [0x00] END_REQSTACK()
```
