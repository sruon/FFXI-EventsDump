# 17335105 - Ungainly Gigas

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Beaucedine Glacier [S] (ID: 136) |
| Block Size       | 72 bytes                         |
| Total Events     | 4                                |
| References Count | 5                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [3](#event-3)            | 0x0001       |      1 |              1 |
| [4](#event-4)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0027      |          39 |
|       2 | 0x20FEE     |      135150 |
|       3 | 0x29838     |      170040 |
|       4 | 0xFFFFB116  |  4294947094 |

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

### Event 3

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

### Event 4

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1C 00 80 32 01  80 1F 00 02 80 03 80 04     ...2.........
0010: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0003 [0x1C] WAIT(30* ticks)
  1: 0x0006 [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  2: 0x0009 [0x1F] MOVE_ENTITY: EventEntity moves to X=135.150*, Z=170.040*, Y=-20.202*
  3: 0x0011 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0013 [0x00] END_REQSTACK()
```
