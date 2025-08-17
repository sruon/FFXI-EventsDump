# 17867246 - Araustoix

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 84 bytes                 |
| Total Events     | 5                        |
| References Count | 5                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [63](#event-63)          | 0x0001       |      1 |              1 |
| [65](#event-65)          | 0x0002       |      1 |              1 |
| [66](#event-66)          | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFEF1      |       65265 |
|       2 | 0xFFFE813F  |  4294869311 |
|       3 | 0x5256      |       21078 |
|       4 | 0x001E      |          30 |

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

### Event 63

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

### Event 65

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

### Event 66

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 1E E1 A1 10 01 1C 04  80 00                    ..........      
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=65.265*, Z=-97.985*, Y=21.078*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x1E] EventEntity looks at Nashu (ID: 17867233/0x0110A1E1) and starts talking
  4: 0x0016 [0x1C] WAIT(30* ticks)
  5: 0x0019 [0x00] END_REQSTACK()
```
