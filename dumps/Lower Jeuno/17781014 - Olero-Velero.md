# 17781014 - Olero-Velero

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 76 bytes              |
| Total Events     | 2                     |
| References Count | 5                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [20079](#event-20079) | 0x0001       |     28 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x2B00      |       11008 |
|       2 | 0x2B01      |       11009 |
|       3 | 0x2B02      |       11010 |
|       4 | 0x2B03      |       11011 |

## String References

- **11008**: Oh, that hideous breath... Its poison-woison is absolutely paralyzing...
- **11009**: In factaru, I love it!
- **11010**: ...
- **11011**: % is not moving.

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

### Event 20079

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 02 10 00 80 00 14  00 1D 01 80 23 1D 02 80   ...........#...
0010: 23 01 1B 00 1D 03 80 23  48 04 80 21 00           #......#H..!.   
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0014
  1: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=11008*)
    → "Oh, that hideous breath... Its poison-woison is absolutely paralyzing..."
  2: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=11009*)
    → "In factaru, I love it!"
  4: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0011 [0x01] GOTO 0x001B
  6: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=11010*)
    → "..."
  7: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0018 [0x48] [System] [11011*]:
    → "% is not moving."

SUBROUTINE_001B:
  9: 0x001B [0x21] END_EVENT
 10: 0x001C [0x00] END_REQSTACK()
```
