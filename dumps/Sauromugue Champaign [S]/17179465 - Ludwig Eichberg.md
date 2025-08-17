# 17179465 - Ludwig Eichberg

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 100 bytes                         |
| Total Events     | 5                                 |
| References Count | 5                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     13 |              3 |
| [65535.2](#event-655352) | 0x0015       |     14 |              4 |
| [10](#event-10)          | 0x0023       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0102      |         258 |
|       1 | 0x000D      |          13 |
|       2 | 0x09E8      |        2536 |
|       3 | 0x12C04     |       76804 |
|       4 | 0xFFFFEC79  |  4294962297 |

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

### Event 9

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
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          6E 49 23 06 01 00 80 99          nI#.....
0010: 49 23 06 01 00                                    I#...           
```

#### Opcodes

```
  0: 0x0008 [0x6E] Ludwig Eichberg (ID: 17179465/0x01062349) uses emote 258*
  1: 0x000F [0x99] Wait for Ludwig Eichberg (ID: 17179465/0x01062349) animation to complete
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                32 01 80  1F 00 02 80 03 80 04 80       2..........
0020: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0015 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.536*, Z=76.804*, Y=-4.999*
  2: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0022 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0023 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0029 [0x00] END_REQSTACK()
```
