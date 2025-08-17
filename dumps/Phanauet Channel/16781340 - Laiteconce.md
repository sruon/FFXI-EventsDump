# 16781340 - Laiteconce

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Phanauet Channel (ID: 1) |
| Block Size       | 68 bytes                 |
| Total Events     | 3                        |
| References Count | 3                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1](#event-1)         | 0x0001       |     11 |              5 |
| [2](#event-2)         | 0x000C       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D04      |        7428 |
|       1 | 0x1D02      |        7426 |
|       2 | 0x1D03      |        7427 |

## String References

- **7426**: This barge is currently en route to [South Landing via Newtpool/Central Landing via the Emfea Waterway/North Landing via the main canal/Central Landing via the main canal].
- **7427**: We should arrive there in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours/about 8 hours/about 9 hours/about 10 hours] ($0 [minute/minutes] in Earth time).
- **7428**: We are nearing [South Landing/Central Landing/North Landing/Central Landing].

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

### Event 1

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
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7428*)
    → "We are nearing [South Landing/Central Landing/North Landing/Central Landing]."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 1D 02 80  23 21 00                 ....#...#!.     
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7426*)
    → "This barge is currently en route to [South Landing via Newtpool/Central Landing via the Emfea Waterway/North Landing via the main canal/Central Landing via the main canal]."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7427*)
    → "We should arrive there in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours/about 8 hours/about 9 hours/about 10 hours] ($0 [minute/minutes] in Earth time)."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```
