# 16994324 - Yohj Dukonlhy

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 152 bytes        |
| Total Events     | 5                |
| References Count | 8                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [231](#event-231)        | 0x0001       |     41 |             12 |
| [65535.1](#event-655351) | 0x002A       |     13 |              7 |
| [65535.2](#event-655352) | 0x0037       |     13 |              7 |
| [65535.3](#event-655353) | 0x0044       |     13 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0090      |         144 |
|       1 | 0x003C      |          60 |
|       2 | 0x0000      |           0 |
|       3 | 0x28F9      |       10489 |
|       4 | 0x28F8      |       10488 |
|       5 | 0x28EF      |       10479 |
|       6 | 0x28F4      |       10484 |
|       7 | 0x28F1      |       10481 |

## String References

- **10479**: The ship to Al Zahbi will soon arrive.
- **10481**: The ferry will depart soon! Passengers are to board the ship immediately!
- **10484**: This ship is headed for Al Zahbi.
- **10488**: The ship bound for Al Zahbi will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time).
- **10489**: The ship bound for Al Zahbi is now [arriving/departing].

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

### Event 231

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 03 04  10 02 10 15 04 10 00 80   ...............
0010: 15 02 10 01 80 02 02 10  02 80 00 24 00 1D 03 80  ...........$....
0020: 23 01 28 00 1D 04 80 23  21 00                    #.(....#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x03] Work_Zone[4] = Work_Zone[2]
  2: 0x000B [0x15] Work_Zone[4] /= 144*
  3: 0x0010 [0x15] Work_Zone[2] /= 60*
  4: 0x0015 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0024
  5: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=10489*)
    → "The ship bound for Al Zahbi is now [arriving/departing]."
  6: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0021 [0x01] GOTO 0x0028
  8: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=10488*)
    → "The ship bound for Al Zahbi will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours] ($0 [minute/minutes] in Earth time)."
  9: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0028:
 10: 0x0028 [0x21] END_EVENT
 11: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                1E F0 FF FF 7F 6F            .....o
0030: 70 1D 05 80 23 21 00                              p...#!.         
```

#### Opcodes

```
  0: 0x002A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0030 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=10479*)
    → "The ship to Al Zahbi will soon arrive."
  4: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0035 [0x21] END_EVENT
  6: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1E  F0 FF FF 7F 6F 70 1D 06         .....op..
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0037 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=10484*)
    → "This ship is headed for Al Zahbi."
  4: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0042 [0x21] END_EVENT
  6: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 6F 70 1D 07 80 23 21      .....op...#!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=10481*)
    → "The ferry will depart soon! Passengers are to board the ship immediately!"
  4: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004F [0x21] END_EVENT
  6: 0x0050 [0x00] END_REQSTACK()
```
