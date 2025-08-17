# 16883718 - Kukki-Chebukki

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 364 bytes                   |
| Total Events     | 10                          |
| References Count | 33                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [101](#event-101)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     30 |              6 |
| [103](#event-103)        | 0x002F       |      1 |              1 |
| [65535.2](#event-655352) | 0x0030       |     54 |              9 |
| [65535.3](#event-655353) | 0x0066       |     14 |              4 |
| [65535.4](#event-655354) | 0x0074       |     14 |              4 |
| [110](#event-110)        | 0x0082       |     10 |              2 |
| [65535.5](#event-655355) | 0x008C       |     15 |              5 |
| [65535.6](#event-655356) | 0x009B       |     18 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE97D  |  4294961533 |
|       1 | 0x1F1F6     |      127478 |
|       2 | 0xFFFF9B1F  |  4294941471 |
|       3 | 0x0C02      |        3074 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFFEC6E  |  4294962286 |
|       6 | 0x1FA98     |      129688 |
|       7 | 0xFFFF9ADA  |  4294941402 |
|       8 | 0x01B9      |         441 |
|       9 | 0x618E      |       24974 |
|      10 | 0x8D16      |       36118 |
|      11 | 0xFFFFD163  |  4294955363 |
|      12 | 0x0BC8      |        3016 |
|      13 | 0x67C1      |       26561 |
|      14 | 0x9E2A      |       40490 |
|      15 | 0xFFFFD11F  |  4294955295 |
|      16 | 0x63E5      |       25573 |
|      17 | 0x9189      |       37257 |
|      18 | 0xFFFFD177  |  4294955383 |
|      19 | 0x6363      |       25443 |
|      20 | 0x6E26      |       28198 |
|      21 | 0xFFFFD1D1  |  4294955473 |
|      22 | 0x13294     |       78484 |
|      23 | 0xDCFA      |       56570 |
|      24 | 0xFFFF76AF  |  4294932143 |
|      25 | 0x0C52      |        3154 |
|      26 | 0x134D3     |       79059 |
|      27 | 0xF93A      |       63802 |
|      28 | 0xFFFF7B0F  |  4294933263 |
|      29 | 0x001E      |          30 |
|      30 | 0x137E6     |       79846 |
|      31 | 0xCA40      |       51776 |
|      32 | 0xFFFF7360  |  4294931296 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-5.763*, z=127.478*, y=-25.825*, direction=270.2°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 6F 5B   2............o[
0020: 08 80 F8 FF FF 7F F8 FF  FF 7F 64 66 6B 30 00     ..........dfk0. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-5.010*, Z=129.688*, Y=-25.894*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dfk0" with entities [EventEntity, EventEntity], work=441*
  5: 0x002E [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               00                 .
```

#### Opcodes

```
  0: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 54 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 04 80 37 09 80 0A 80  0B 80 0C 80 22 00 1F 00  2..7........"...
0040: 0D 80 0E 80 0F 80 1F 01  6F 5B 08 80 06 A0 01 01  ........o[......
0050: 06 A0 01 01 64 66 6B 30  53 06 A0 01 01 06 A0 01  ....dfk0S.......
0060: 01 64 66 6D 30 00                                 .dfm0.          
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0033 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=24.974*, z=36.118*, y=-11.933*, direction=265.1°*
  2: 0x003C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=26.561*, Z=40.490*, Y=-12.001*
  4: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0049 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dfk0" with entities [Kukki-Chebukki (ID: 16883718/0x0101A006), Kukki-Chebukki (ID: 16883718/0x0101A006)], work=441*
  7: 0x0058 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dfm0" with entities [Kukki-Chebukki (ID: 16883718/0x0101A006), Kukki-Chebukki (ID: 16883718/0x0101A006)]
  8: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   32 04  80 1F 00 10 80 11 80 12        2.........
0070: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0066 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=25.573*, Z=37.257*, Y=-11.913*
  2: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0073 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0074   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             32 04 80 1F  00 13 80 14 80 15 80 1F      2...........
0080: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0074 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0077 [0x1F] MOVE_ENTITY: EventEntity moves to X=25.443*, Z=28.198*, Y=-11.823*
  2: 0x007F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0081 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0082   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:       37 16 80 17 80 18  80 19 80 00                7.........    
```

#### Opcodes

```
  0: 0x0082 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=78.484*, z=56.570*, y=-35.153*, direction=277.2°*
  1: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      32 04 80 1F              2...
0090: 00 1A 80 1B 80 1C 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x008C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x008F [0x1F] MOVE_ENTITY: EventEntity moves to X=79.059*, Z=63.802*, Y=-34.033*
  2: 0x0097 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0099 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   1C 1D 80 32 04             ...2.
00A0: 80 1F 00 1E 80 1F 80 20  80 1F 01 6F 00           ....... ...o.   
```

#### Opcodes

```
  0: 0x009B [0x1C] WAIT(30* ticks)
  1: 0x009E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=79.846*, Z=51.776*, Y=-36.000*
  3: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00AC [0x00] END_REQSTACK()
```
