# 17494809 - Red Rose Condottiere

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 164 bytes                            |
| Total Events     | 4                                    |
| References Count | 16                                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [49](#event-49)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     15 |              5 |
| [65535.2](#event-655352) | 0x0017       |     45 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFC6D02  |  4294733058 |
|       2 | 0x1B577     |      111991 |
|       3 | 0x047B      |        1147 |
|       4 | 0xFFFC5659  |  4294727257 |
|       5 | 0x1CD43     |      118083 |
|       6 | 0x03E8      |        1000 |
|       7 | 0xFFFC239A  |  4294714266 |
|       8 | 0x20663     |      132707 |
|       9 | 0x0106      |         262 |
|      10 | 0xFFFC0E7F  |  4294708863 |
|      11 | 0x229A2     |      141730 |
|      12 | 0xFFFFFFDC  |  4294967260 |
|      13 | 0xFFFC0C01  |  4294708225 |
|      14 | 0x263C3     |      156611 |
|      15 | 0x006B      |         107 |

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

### Event 49

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-234.238*, Z=111.991*, Y=1.147*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  00 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 1F 00 07 80  08 80 09 80 1F 01 1F 00  ................
0030: 0A 80 0B 80 0C 80 1F 01  1F 00 0D 80 0E 80 0F 80  ................
0040: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-240.039*, Z=118.083*, Y=1.000*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-253.030*, Z=132.707*, Y=0.262*
  4: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=-258.433*, Z=141.730*, Y=-0.036*
  6: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=-259.071*, Z=156.611*, Y=0.107*
  8: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x0043 [0x00] END_REQSTACK()
```
