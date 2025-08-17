# 17371592 - Ghoo Pakya

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Giddeus (ID: 145) |
| Block Size       | 116 bytes         |
| Total Events     | 5                 |
| References Count | 6                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [49](#event-49)       | 0x0001       |     12 |              6 |
| [50](#event-50)       | 0x000D       |     11 |              5 |
| [51](#event-51)       | 0x0018       |     19 |              9 |
| [52](#event-52)       | 0x002B       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CBE      |        7358 |
|       1 | 0x1CBF      |        7359 |
|       2 | 0x1CC0      |        7360 |
|       3 | 0x1CC1      |        7361 |
|       4 | 0x1CC2      |        7362 |
|       5 | 0x1CBD      |        7357 |

## String References

- **7357**: Kyah! No time for smoothskins who carry no food offering! You be crawling away now, before my brethren sacrifice you instead! Kyah!
- **7358**: You be coming long way to deliver this, kyah? You be telling other smoothskins to keep offerings coming! Kyah-kyah-kyah!
- **7359**: Kyah!? Smoothskin wants to take offering back? Smoothskin wanting to destroy friendship, kyah?
- **7360**: Altars be directly connecting to treasure chamber.
- **7361**: Kyah! Smoothskin wanting it back so much, then smoothskin be crawling to treasure chamber on own hands and feets!
- **7362**: We be not caring for your reasons. My brethren will not be taking this intrusion quietly! Kyah-kyah-kyah!

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1D  00 80 23 21 00            B........#!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=7358*)
    → "You be coming long way to deliver this, kyah? You be telling other smoothskins to keep offerings coming! Kyah-kyah-kyah!"
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x21] END_EVENT
  5: 0x000C [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         1E F0 FF               ...
0010: FF 7F 1D 01 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=7359*)
    → "Kyah!? Smoothskin wants to take offering back? Smoothskin wanting to destroy friendship, kyah?"
  2: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0016 [0x21] END_EVENT
  4: 0x0017 [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          1E F0 FF FF 7F 1D 02 80          ........
0020: 23 1D 03 80 23 1D 04 80  23 21 00                 #...#...#!.     
```

#### Opcodes

```
  0: 0x0018 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=7360*)
    → "Altars be directly connecting to treasure chamber."
  2: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7361*)
    → "Kyah! Smoothskin wanting it back so much, then smoothskin be crawling to treasure chamber on own hands and feets!"
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7362*)
    → "We be not caring for your reasons. My brethren will not be taking this intrusion quietly! Kyah-kyah-kyah!"
  6: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0029 [0x21] END_EVENT
  8: 0x002A [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   1E F0 FF FF 7F             .....
0030: 1D 05 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x002B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=7357*)
    → "Kyah! No time for smoothskins who carry no food offering! You be crawling away now, before my brethren sacrifice you instead! Kyah!"
  2: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0034 [0x21] END_EVENT
  4: 0x0035 [0x00] END_REQSTACK()
```
