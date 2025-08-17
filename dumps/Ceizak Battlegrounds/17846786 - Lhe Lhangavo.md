# 17846786 - Lhe Lhangavo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 116 bytes                      |
| Total Events     | 4                              |
| References Count | 7                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [19](#event-19)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     22 |              6 |
| [65535.2](#event-655352) | 0x001E       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFD75CD  |  4294800845 |
|       2 | 0xFFFF6AD4  |  4294929108 |
|       3 | 0x0000      |           0 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFD7579  |  4294800761 |
|       6 | 0xFFFF5C28  |  4294925352 |

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

### Event 19

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 1E F0 FF  FF 7F 1C 04 80 00        ..............  
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-166.451*, Z=-38.188*, Y=0.000*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x001A [0x1C] WAIT(30* ticks)
  5: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            32 00                2.
0020: 80 1F 00 05 80 06 80 03  80 1F 01 6F 4A F0 FF FF  ...........oJ...
0030: 7F 02 52 10 01 00                                 ..R...          
```

#### Opcodes

```
  0: 0x001E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=-166.535*, Z=-41.944*, Y=0.000*
  2: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002C [0x4A] LocalPlayer looks at Lhe Lhangavo (ID: 17846786/0x01105202)
  5: 0x0035 [0x00] END_REQSTACK()
```
