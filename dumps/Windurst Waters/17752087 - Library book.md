# 17752087 - Library book

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 108 bytes                 |
| Total Events     | 2                         |
| References Count | 6                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [367](#event-367)     | 0x0001       |     56 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FDD      |        8157 |
|       1 | 0x1FDE      |        8158 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x1FDF      |        8159 |
|       5 | 0x1FE0      |        8160 |

## String References

- **8157**: There's a suspicious-looking book here...
- **8158**: Check its contents? [No way!/Take a peek.]
- **8159**: Oh, no! You've been cursed!
- **8160**: ...or so you thought for a second there.

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

### Event 367

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 56 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 1D 00 03 01 10  02 80 01 35 00 02 00 10  ...........5....
0020: 03 80 00 35 00 03 01 10  03 80 48 04 80 23 48 05  ...5......H..#H.
0030: 80 23 01 35 00 20 00 21  00                       .#.5. .!.       
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [8157*]:
    → "There's a suspicious-looking book here..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=8158*, default_option=0*, option_flags=0*)
    → "Check its contents? [No way!/Take a peek.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001D
  5: 0x0015 [0x03] Work_Zone[1] = 0*
  6: 0x001A [0x01] GOTO 0x0035
  7: 0x001D [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0035
  8: 0x0025 [0x03] Work_Zone[1] = 1*
  9: 0x002A [0x48] [System] [8159*]:
    → "Oh, no! You've been cursed!"
 10: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002E [0x48] [System] [8160*]:
    → "...or so you thought for a second there."
 12: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0032 [0x01] GOTO 0x0035

SUBROUTINE_0035:
 14: 0x0035 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x0037 [0x21] END_EVENT
 16: 0x0038 [0x00] END_REQSTACK()
```
