# 17469798 - Karaha-Baruha

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Toraimarai Canal (ID: 169) |
| Block Size       | 152 bytes                  |
| Total Events     | 10                         |
| References Count | 11                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [41](#event-41)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |      5 |              3 |
| [65535.3](#event-655353) | 0x0015       |      5 |              3 |
| [65535.4](#event-655354) | 0x001A       |      5 |              3 |
| [65535.5](#event-655355) | 0x001F       |      5 |              3 |
| [65535.6](#event-655356) | 0x0024       |      5 |              3 |
| [65535.7](#event-655357) | 0x0029       |      5 |              3 |
| [65535.8](#event-655358) | 0x002E       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x22ED7     |      143063 |
|       2 | 0xFFFFBAC4  |  4294949572 |
|       3 | 0x32C7      |       12999 |
|       4 | 0x1D0F      |        7439 |
|       5 | 0x1D10      |        7440 |
|       6 | 0x1D11      |        7441 |
|       7 | 0x1D13      |        7443 |
|       8 | 0x1D17      |        7447 |
|       9 | 0x1D18      |        7448 |
|      10 | 0x1D19      |        7449 |

## String References

- **7439**: Yes, I would like to name this magic "summoning."
- **7440**: The divine texts mention it as the words used when the Star Sibyl was commanding the great beast, Fenrir.
- **7441**: At any rate, we are very close. Soon the magic of summoning will be complete.
- **7443**: Are you uneasy, Your Holiness?
- **7447**: Place your trust in me, Your Holiness. Windurst shall escape its fate of ruin.
- **7448**: The Book of the Gods has taught me everything.
- **7449**: It told me the meaning of the tower and the fountain. And it has taught me what the beast Fenrir truly is.

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

### Event 41

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=143.063*, Z=-17.724*, Y=12.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1D 04 80 23 00                                    ...#.           
```

#### Opcodes

```
  0: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7439*)
    → "Yes, I would like to name this magic "summoning.""
  1: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                1D 05 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7440*)
    → "The divine texts mention it as the words used when the Star Sibyl was commanding the great beast, Fenrir."
  1: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1D 06 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7441*)
    → "At any rate, we are very close. Soon the magic of summoning will be complete."
  1: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1D                 .
0020: 07 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7443*)
    → "Are you uneasy, Your Holiness?"
  1: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1D 08 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7447*)
    → "Place your trust in me, Your Holiness. Windurst shall escape its fate of ruin."
  1: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1D 09 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7448*)
    → "The Book of the Gods has taught me everything."
  1: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            1D 0A                ..
0030: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7449*)
    → "It told me the meaning of the tower and the fountain. And it has taught me what the beast Fenrir truly is."
  1: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0032 [0x00] END_REQSTACK()
```
