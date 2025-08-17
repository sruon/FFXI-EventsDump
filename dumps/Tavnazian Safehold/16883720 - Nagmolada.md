# 16883720 - Nagmolada

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 312 bytes                   |
| Total Events     | 9                           |
| References Count | 30                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [101](#event-101)        | 0x000D       |     10 |              2 |
| [103](#event-103)        | 0x0017       |      1 |              1 |
| [65535.1](#event-655351) | 0x0018       |     25 |              6 |
| [110](#event-110)        | 0x0031       |     10 |              2 |
| [65535.2](#event-655352) | 0x003B       |     35 |              8 |
| [65535.3](#event-655353) | 0x005E       |     15 |              5 |
| [65535.4](#event-655354) | 0x006D       |     15 |              5 |
| [65535.5](#event-655355) | 0x007C       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFEF16  |  4294962966 |
|       1 | 0x20520     |      132384 |
|       2 | 0xFFFF9AB1  |  4294941361 |
|       3 | 0x0383      |         899 |
|       4 | 0x000D      |          13 |
|       5 | 0x68C3      |       26819 |
|       6 | 0x9C16      |       39958 |
|       7 | 0xFFFFD14E  |  4294955342 |
|       8 | 0x0C22      |        3106 |
|       9 | 0x6C33      |       27699 |
|      10 | 0xA61A      |       42522 |
|      11 | 0xFFFFD120  |  4294955296 |
|      12 | 0x15000     |       86016 |
|      13 | 0xE957      |       59735 |
|      14 | 0xFFFF7BF3  |  4294933491 |
|      15 | 0x0B1C      |        2844 |
|      16 | 0x14CC1     |       85185 |
|      17 | 0xF085      |       61573 |
|      18 | 0xFFFF7B72  |  4294933362 |
|      19 | 0x13B86     |       80774 |
|      20 | 0xFAF6      |       64246 |
|      21 | 0xFFFF7B30  |  4294933296 |
|      22 | 0x13953     |       80211 |
|      23 | 0xFE06      |       65030 |
|      24 | 0xFFFF7B3B  |  4294933307 |
|      25 | 0x12D93     |       77203 |
|      26 | 0xFD33      |       64819 |
|      27 | 0x12FFF     |       77823 |
|      28 | 0xD8A9      |       55465 |
|      29 | 0xFFFF75D4  |  4294931924 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-4.330*, z=132.384*, y=-25.935*, direction=79.0°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 04 80 37 05 80 06 80          2..7....
0020: 07 80 08 80 22 00 1F 00  09 80 0A 80 0B 80 1F 01  ...."...........
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=26.819*, z=39.958*, y=-11.954*, direction=273.0°*
  2: 0x0024 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=27.699*, Z=42.522*, Y=-12.000*
  4: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0030 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    37 0C 80 0D 80 0E 80  0F 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0031 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=86.016*, z=59.735*, y=-33.805*, direction=250.0°*
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 35 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 04 80 1F 00             2....
0040: 10 80 11 80 12 80 1F 01  79 00 F8 FF FF 7F F0 FF  ........y.......
0050: FF 7F 1F 00 13 80 14 80  15 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=85.185*, Z=61.573*, Y=-33.934*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x79] EventEntity looks at LocalPlayer (Basic look)
  4: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=80.774*, Z=64.246*, Y=-34.000*
  5: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 04                2.
0060: 80 1F 00 16 80 17 80 18  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=80.211*, Z=65.030*, Y=-33.989*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 04 80               2..
0070: 1F 00 19 80 1A 80 15 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=77.203*, Z=64.819*, Y=-34.000*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      32 04 80 1F              2...
0080: 00 1B 80 1C 80 1D 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x007C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=77.823*, Z=55.465*, Y=-35.372*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008A [0x00] END_REQSTACK()
```
