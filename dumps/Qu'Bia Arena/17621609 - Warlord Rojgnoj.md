# 17621609 - Warlord Rojgnoj

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qu'Bia Arena (ID: 206) |
| Block Size       | 360 bytes              |
| Total Events     | 16                     |
| References Count | 25                     |

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
| [32000](#event-32000)      | 0x0044       |      1 |              1 |
| [32004](#event-32004)      | 0x0045       |      1 |              1 |
| [65535.7](#event-655357)   | 0x0046       |     15 |              5 |
| [65535.8](#event-655358)   | 0x0055       |     10 |              2 |
| [65535.9](#event-655359)   | 0x005F       |     10 |              2 |
| [65535.10](#event-6553510) | 0x0069       |     15 |              5 |
| [32001](#event-32001)      | 0x0078       |     10 |              2 |
| [65535.11](#event-6553511) | 0x0082       |     49 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000A      |          10 |
|       4 | 0xFFF9E57F  |  4294567295 |
|       5 | 0x59478     |      365688 |
|       6 | 0xFFFCC87E  |  4294756478 |
|       7 | 0xFFF9E52E  |  4294567214 |
|       8 | 0x5A209     |      369161 |
|       9 | 0xFFFCC9DF  |  4294756831 |
|      10 | 0x0C08      |        3080 |
|      11 | 0xFFF9E539  |  4294567225 |
|      12 | 0x5F67D     |      390781 |
|      13 | 0xFFFCEC68  |  4294765672 |
|      14 | 0x0C02      |        3074 |
|      15 | 0x0009      |           9 |
|      16 | 0xFFF9E710  |  4294567696 |
|      17 | 0x605B8     |      394680 |
|      18 | 0xFFFCEC67  |  4294765671 |
|      19 | 0xFFF9E567  |  4294567271 |
|      20 | 0x60906     |      395526 |
|      21 | 0x0C1D      |        3101 |
|      22 | 0x0018      |          24 |
|      23 | 0x0046      |          70 |
|      24 | 0x00F3      |         243 |

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

### Event 32000

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

### Event 32004

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 03  80 1F 00 04 80 05 80 06        2.........
0050: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=-400.001*, Z=365.688*, Y=-210.818*
  2: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                37 07 80  08 80 09 80 0A 80 00          7......... 
```

#### Opcodes

```
  0: 0x0055 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-400.082*, z=369.161*, y=-210.465*, direction=270.7°*
  1: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               37                 7
0060: 0B 80 0C 80 0D 80 0E 80  00                       .........       
```

#### Opcodes

```
  0: 0x005F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-400.071*, z=390.781*, y=-201.624*, direction=270.2°*
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             32 0F 80 1F 00 10 80           2......
0070: 11 80 12 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0069 [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x006C [0x1F] MOVE_ENTITY: EventEntity moves to X=-399.600*, Z=394.680*, Y=-201.625*
  2: 0x0074 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0076 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0077 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          37 13 80 14 80 12 80 15          7.......
0080: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0078 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-400.025*, z=395.526*, y=-201.625*, direction=272.5°*
  1: 0x0081 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 49 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       5B 16 80 F8 FF FF  7F F8 FF FF 7F 64 6F 77    [..........dow
0090: 6E 1C 17 80 45 18 80 F8  FF FF 7F F8 FF FF 7F 73  n...E..........s
00A0: 65 30 39 00 80 53 F8 FF  FF 7F F8 FF FF 7F 64 61  e09..S........da
00B0: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x0082 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "down" with entities [EventEntity, EventEntity], work=24*
  1: 0x0091 [0x1C] WAIT(70* ticks)
  2: 0x0094 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se09" with entities [EventEntity, EventEntity], work=[243*, 0*]
  3: 0x00A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dai0" with entities [EventEntity, EventEntity]
  4: 0x00B2 [0x00] END_REQSTACK()
```
