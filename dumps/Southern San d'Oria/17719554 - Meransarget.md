# 17719554 - Meransarget

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 388 bytes                     |
| Total Events     | 17                            |
| References Count | 31                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [757](#event-757)          | 0x0044       |      1 |              1 |
| [758](#event-758)          | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0050       |     10 |              2 |
| [65535.10](#event-6553510) | 0x005A       |     15 |              5 |
| [65535.11](#event-6553511) | 0x0069       |     24 |              6 |
| [65535.12](#event-6553512) | 0x0081       |     10 |              2 |
| [65535.13](#event-6553513) | 0x008B       |     15 |              5 |
| [65535.14](#event-6553514) | 0x009A       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0xFFFB61D8  |  4294664664 |
|       4 | 0x182A3     |       98979 |
|       5 | 0xFFFFDC11  |  4294958097 |
|       6 | 0x0120      |         288 |
|       7 | 0xFFFBC2CE  |  4294689486 |
|       8 | 0x17E93     |       97939 |
|       9 | 0xFFFFE7C9  |  4294961097 |
|      10 | 0x0FE3      |        4067 |
|      11 | 0x000B      |          11 |
|      12 | 0xFFFBD401  |  4294693889 |
|      13 | 0x17EB8     |       97976 |
|      14 | 0xFFFBF124  |  4294701348 |
|      15 | 0x17F14     |       98068 |
|      16 | 0xFFFFF060  |  4294963296 |
|      17 | 0x003D      |          61 |
|      18 | 0xFFFBFE5A  |  4294704730 |
|      19 | 0x17EE1     |       98017 |
|      20 | 0xFFFC2475  |  4294714485 |
|      21 | 0x17EA6     |       97958 |
|      22 | 0xFFFFF061  |  4294963297 |
|      23 | 0x08FC      |        2300 |
|      24 | 0x0009      |           9 |
|      25 | 0xFFFC3050  |  4294717520 |
|      26 | 0x17EE7     |       98023 |
|      27 | 0xFFFC5391  |  4294726545 |
|      28 | 0xFFFC7A02  |  4294736386 |
|      29 | 0x17E92     |       97938 |
|      30 | 0xFFFFF830  |  4294965296 |

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

### Event 65535.2

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

### Event 65535.3

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

### Event 65535.4

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

### Event 65535.5

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

### Event 65535.6

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

### Event 65535.7

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

### Event 757

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

### Event 758

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

### Event 65535.8

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
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-302.632*, z=98.979*, y=-9.199*, direction=25.3°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 37 07 80 08 80 09 80 0A  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0050 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-277.810*, z=97.939*, y=-6.199*, direction=357.4°*
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 0B 80 1F 00 0C            2.....
0060: 80 0D 80 09 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=-273.407*, Z=97.976*, Y=-6.199*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             37 0E 80 0F 80 10 80           7......
0070: 11 80 1C 01 80 1F 00 12  80 13 80 10 80 1F 01 6F  ...............o
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0069 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-265.948*, z=98.068*, y=-4.000*, direction=5.4°*
  1: 0x0072 [0x1C] WAIT(1* ticks)
  2: 0x0075 [0x1F] MOVE_ENTITY: EventEntity moves to X=-262.566*, Z=98.017*, Y=-4.000*
  3: 0x007D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x007F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    37 14 80 15 80 16 80  17 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0081 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-252.811*, z=97.958*, y=-3.999*, direction=202.1°*
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   32 18 80 1F 00             2....
0090: 19 80 1A 80 10 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x008B [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x008E [0x1F] MOVE_ENTITY: EventEntity moves to X=-249.776*, Z=98.023*, Y=-4.000*
  2: 0x0096 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0098 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                32 0B 80 1F 00 1B            2.....
00A0: 80 15 80 10 80 1F 01 1F  00 1C 80 1D 80 1E 80 1F  ................
00B0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x009A [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x009D [0x1F] MOVE_ENTITY: EventEntity moves to X=-240.751*, Z=97.958*, Y=-4.000*
  2: 0x00A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-230.910*, Z=97.938*, Y=-2.000*
  4: 0x00AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B1 [0x00] END_REQSTACK()
```
