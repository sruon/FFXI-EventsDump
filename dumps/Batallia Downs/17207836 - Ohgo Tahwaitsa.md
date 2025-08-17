# 17207836 - Ohgo Tahwaitsa

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 236 bytes                |
| Total Events     | 6                        |
| References Count | 26                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [904](#event-904)        | 0x0001       |     19 |              3 |
| [65535.1](#event-655351) | 0x0014       |     14 |              4 |
| [65535.2](#event-655352) | 0x0022       |     10 |              2 |
| [65535.3](#event-655353) | 0x002C       |     27 |              7 |
| [65535.4](#event-655354) | 0x0047       |     19 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x34AFD     |      215805 |
|       1 | 0xFFF6FC16  |  4294376470 |
|       2 | 0x3085      |       12421 |
|       3 | 0x03A8      |         936 |
|       4 | 0x3497F     |      215423 |
|       5 | 0xFFF6F2AB  |  4294374059 |
|       6 | 0x3239      |       12857 |
|       7 | 0x044C      |        1100 |
|       8 | 0x000D      |          13 |
|       9 | 0x34813     |      215059 |
|      10 | 0xFFF6E9AE  |  4294371758 |
|      11 | 0x340A      |       13322 |
|      12 | 0x0C6C      |        3180 |
|      13 | 0x0028      |          40 |
|      14 | 0x332A6     |      209574 |
|      15 | 0xFFF6DE36  |  4294368822 |
|      16 | 0x3961      |       14689 |
|      17 | 0x00B4      |         180 |
|      18 | 0x001E      |          30 |
|      19 | 0x34541     |      214337 |
|      20 | 0xFFF6D735  |  4294367029 |
|      21 | 0x3514      |       13588 |
|      22 | 0x003C      |          60 |
|      23 | 0x322EE     |      205550 |
|      24 | 0xFFF70EAE  |  4294381230 |
|      25 | 0x3B9B      |       15259 |

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

### Event 904

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 37 04 80 05 80 06   7........7.....
0010: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=215.805*, z=-590.826*, y=12.421*, direction=82.3°*
  1: 0x000A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=215.423*, z=-593.237*, y=12.857*, direction=96.7°*
  2: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             32 08 80 1F  00 09 80 0A 80 0B 80 1F      2...........
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0014 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=215.059*, Z=-595.538*, Y=13.322*
  2: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       37 09 80 0A 80 0B  80 0C 80 00                7.........    
```

#### Opcodes

```
  0: 0x0022 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=215.059*, z=-595.538*, y=13.322*, direction=279.5°*
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 0D 80 37              2..7
0030: 0E 80 0F 80 10 80 11 80  1C 12 80 1F 00 13 80 14  ................
0040: 80 15 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=209.574*, z=-598.474*, y=14.689*, direction=15.8°*
  2: 0x0038 [0x1C] WAIT(30* ticks)
  3: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=214.337*, Z=-600.267*, Y=13.588*
  4: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0045 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 19 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      1C  16 80 32 08 80 1F 00 17         ...2.....
0050: 80 18 80 19 80 1F 01 22  01 00                    ......."..      
```

#### Opcodes

```
  0: 0x0047 [0x1C] WAIT(60* ticks)
  1: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=205.550*, Z=-586.066*, Y=15.259*
  3: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0057 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  5: 0x0059 [0x00] END_REQSTACK()
```
