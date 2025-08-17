# 16793982 - Fheli Lapatzuo

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Bibiki Bay (ID: 4) |
| Block Size       | 92 bytes           |
| Total Events     | 3                  |
| References Count | 5                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [18](#event-18)       | 0x0001       |     41 |             12 |
| [36](#event-36)       | 0x002A       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0090      |         144 |
|       1 | 0x003C      |          60 |
|       2 | 0x0000      |           0 |
|       3 | 0x1C46      |        7238 |
|       4 | 0x1C45      |        7237 |

## String References

- **7237**: The manaclipper bound for [Dhalmel Rock/Maliyakaleya Reef/Purgonorgo Isle/Sunset Docks] will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours/about 8 hours/about 9 hours/about 10 hours] ($0 [minute/minutes] in Earth time).
- **7238**: The manaclipper bound for [Dhalmel Rock/Maliyakaleya Reef/Purgonorgo Isle/Sunset Docks] will [arrive/depart] shortly.

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

### Event 18

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
  5: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=7238*)
    → "The manaclipper bound for [Dhalmel Rock/Maliyakaleya Reef/Purgonorgo Isle/Sunset Docks] will [arrive/depart] shortly."
  6: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0021 [0x01] GOTO 0x0028
  8: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7237*)
    → "The manaclipper bound for [Dhalmel Rock/Maliyakaleya Reef/Purgonorgo Isle/Sunset Docks] will [arrive/depart] in [less than an hour/about 1 hour/about 2 hours/about 3 hours/about 4 hours/about 5 hours/about 6 hours/about 7 hours/about 8 hours/about 9 hours/about 10 hours] ($0 [minute/minutes] in Earth time)."
  9: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0028:
 10: 0x0028 [0x21] END_EVENT
 11: 0x0029 [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```
