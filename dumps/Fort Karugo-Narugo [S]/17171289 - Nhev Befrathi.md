# 17171289 - Nhev Befrathi

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Fort Karugo-Narugo [S] (ID: 96) |
| Block Size       | 236 bytes                       |
| Total Events     | 13                              |
| References Count | 17                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [115](#event-115)        | 0x0000       |      1 |              1 |
| [116](#event-116)        | 0x0001       |      1 |              1 |
| [117](#event-117)        | 0x0002       |      1 |              1 |
| [118](#event-118)        | 0x0003       |      1 |              1 |
| [119](#event-119)        | 0x0004       |      1 |              1 |
| [120](#event-120)        | 0x0005       |      1 |              1 |
| [65535](#event-65535)    | 0x0006       |     10 |              2 |
| [65535.1](#event-655351) | 0x0010       |     10 |              2 |
| [65535.2](#event-655352) | 0x001A       |     15 |              5 |
| [65535.3](#event-655353) | 0x0029       |     19 |              5 |
| [65535.4](#event-655354) | 0x003C       |     19 |              5 |
| [65535.5](#event-655355) | 0x004F       |     19 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFF9176E  |  4294514542 |
|       5 | 0x536B8     |      341688 |
|       6 | 0xFFFF9974  |  4294941044 |
|       7 | 0xFFF91B7F  |  4294515583 |
|       8 | 0x5354F     |      341327 |
|       9 | 0xFFFF98A1  |  4294940833 |
|      10 | 0xFFF9CA01  |  4294560257 |
|      11 | 0x5710A     |      356618 |
|      12 | 0xFFFF9337  |  4294939447 |
|      13 | 0x0010      |          16 |
|      14 | 0xFFF97A10  |  4294539792 |
|      15 | 0x54A12     |      346642 |
|      16 | 0xFFFF91D7  |  4294939095 |

## Events

### Event 115

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

### Event 116

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

### Event 117

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 119

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   6C 59  03 06 01 00 80 01 80 00        lY........
```

#### Opcodes

```
  0: 0x0006 [0x6C] FADE_ENTITY_COLOR(entity_id=Nhev Befrathi (ID: 17171289/0x01060359), end_alpha=0*, fade_time=1*)
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 6C 59 03 06 01 02 80 01  80 00                    lY........      
```

#### Opcodes

```
  0: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=Nhev Befrathi (ID: 17171289/0x01060359), end_alpha=128*, fade_time=1*)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 03 80 1F 00 04            2.....
0020: 80 05 80 06 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-452.754*, Z=341.688*, Y=-26.252*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             32 03 80 1F 00 07 80           2......
0030: 08 80 09 80 1F 01 1E F0  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x0029 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=-451.713*, Z=341.327*, Y=-26.463*
  2: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0036 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 03 80 1F              2...
0040: 00 0A 80 0B 80 0C 80 1F  01 1E F0 FF FF 7F 00     ............... 
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=-407.039*, Z=356.618*, Y=-27.849*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 0D 80 1F 00 0E 80 0F 80  10 80 1F 01 1E 5A 03 06  .............Z..
0060: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 16* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-427.504*, Z=346.642*, Y=-28.201*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x1E] EventEntity looks at Syu Befrathi (ID: 17171290/0x0106035A) and starts talking
  4: 0x0061 [0x00] END_REQSTACK()
```
