# 17047809 - Rune of Release

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Mamool Ja Training Grounds (ID: 66) |
| Block Size       | 76 bytes                            |
| Total Events     | 2                                   |
| References Count | 3                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |     37 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C9B      |        7323 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |

## String References

- **7323**: Leave [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll]? [Yes./No.]

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
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 02 80  25 02 00 10 02 80 00 19   $......%.......
0010: 00 03 01 10 01 80 01 24  00 02 00 10 01 80 00 24  .......$.......$
0020: 00 01 24 00 21 00                                 ..$.!.          
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7323*, default_option=1*, option_flags=0*)
    → "Leave [Leujaoam Sanctum/the Mamool Ja Training Grounds/Lebros Cavern/Periqia/Ilrusi Atoll]? [Yes./No.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 1*
  4: 0x0016 [0x01] GOTO 0x0024
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0024
  6: 0x0021 [0x01] GOTO 0x0024

SUBROUTINE_0024:
  7: 0x0024 [0x21] END_EVENT
  8: 0x0025 [0x00] END_REQSTACK()
```
