# 17747975 - Dark Clouds

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 100 bytes            |
| Total Events     | 4                    |
| References Count | 7                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [100](#event-100)        | 0x0001       |     11 |              5 |
| [922](#event-922)        | 0x000C       |      1 |              1 |
| [65535.1](#event-655351) | 0x000D       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D26      |        7462 |
|       1 | 0x0028      |          40 |
|       2 | 0xFFFEAB5B  |  4294880091 |
|       3 | 0xFFFFDE46  |  4294958662 |
|       4 | 0x07D0      |        2000 |
|       5 | 0xFFFEC7D1  |  4294887377 |
|       6 | 0xFFFFD5F9  |  4294956537 |

## String References

- **7462**: This is Bastok's Blacksmiths' Guild. Ours is the real thing--the one in San d'Oria doesn't have half the things we do!

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

### Event 100

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7462*)
    → "This is Bastok's Blacksmiths' Guild. Ours is the real thing--the one in San d'Oria doesn't have half the things we do!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 922

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      00                       .   
```

#### Opcodes

```
  0: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         32 01 80               2..
0010: 1F 00 02 80 03 80 04 80  1F 01 1F 00 05 80 06 80  ................
0020: 04 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x000D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-87.205*, Z=-8.634*, Y=2.000*
  2: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=-79.919*, Z=-10.759*, Y=2.000*
  4: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0024 [0x00] END_REQSTACK()
```
