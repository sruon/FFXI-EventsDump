# 17772754 - King of Hearts

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 76 bytes                  |
| Total Events     | 4                         |
| References Count | 5                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10098](#event-10098)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     15 |              5 |
| [65535.2](#event-655352) | 0x0011       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFFFB56  |  4294966102 |
|       2 | 0x1593E     |       88382 |
|       3 | 0x07D0      |        2000 |
|       4 | 0x0186      |         390 |

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

### Event 10098

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.194*, Z=88.382*, Y=2.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    39 04 80 00                                     9...           
```

#### Opcodes

```
  0: 0x0011 [0x39] SET_ENTITY_DIRECTION(direction=2.1°*)
  1: 0x0014 [0x00] END_REQSTACK()
```
