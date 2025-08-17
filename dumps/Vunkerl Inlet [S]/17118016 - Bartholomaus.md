# 17118016 - Bartholomaus

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Vunkerl Inlet [S] (ID: 83) |
| Block Size       | 168 bytes                  |
| Total Events     | 6                          |
| References Count | 13                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [113](#event-113)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     14 |              4 |
| [65535.2](#event-655352) | 0x0016       |     16 |              4 |
| [65535.3](#event-655353) | 0x0026       |     22 |              6 |
| [65535.4](#event-655354) | 0x003C       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFA832F  |  4294607663 |
|       2 | 0x44C61     |      281697 |
|       3 | 0xFFFF8300  |  4294935296 |
|       4 | 0x0019      |          25 |
|       5 | 0x00B4      |         180 |
|       6 | 0xFFF9C4D6  |  4294558934 |
|       7 | 0x44674     |      280180 |
|       8 | 0xFFFF7F7E  |  4294934398 |
|       9 | 0x001E      |          30 |
|      10 | 0x000D      |          13 |
|      11 | 0xFFF98775  |  4294543221 |
|      12 | 0x44632     |      280114 |

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

### Event 113

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 5A 00 01 80 02          2..Z....
0010: 80 03 80 5A 01 00                                 ...Z..          
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-359.633*, Z=281.697*, Y=-32.000*
  2: 0x0013 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   6E 40  33 05 01 04 80 99 40 33        n@3.....@3
0020: 05 01 1C 05 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0016 [0x6E] Bartholomaus (ID: 17118016/0x01053340) uses emote 25*
  1: 0x001D [0x99] Wait for Bartholomaus (ID: 17118016/0x01053340) animation to complete
  2: 0x0022 [0x1C] WAIT(180* ticks)
  3: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 00  80 1F 00 06 80 07 80 08        2.........
0030: 80 1F 01 1E 3C 33 05 01  1C 09 80 00              ....<3......    
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=-408.362*, Z=280.180*, Y=-32.898*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x1E] EventEntity looks at Klara (ID: 17118012/0x0105333C) and starts talking
  4: 0x0038 [0x1C] WAIT(30* ticks)
  5: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 0A 80 1F              2...
0040: 00 0B 80 0C 80 08 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=-424.075*, Z=280.114*, Y=-32.898*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x00] END_REQSTACK()
```
