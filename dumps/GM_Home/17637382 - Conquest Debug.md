# 17637382 - Conquest Debug

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 60 bytes          |
| Total Events     | 2                 |
| References Count | 2                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     26 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BA1      |        7073 |
|       1 | 0x0000      |           0 |

## String References

- **7073**: Vat do you vant? [Conquest points!/1 day gone (Vana'diel time)/1 day gone (earth time)/1 week gone (earth time)/Supplies for supply quest!/Not much at the moment.]

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 14   $......%.......
0010: 00 01 14 00 03 01 10 00  10 21 00                 .........!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7073*, default_option=0*, option_flags=0*)
    → "Vat do you vant? [Conquest points!/1 day gone (Vana'diel time)/1 day gone (earth time)/1 week gone (earth time)/Supplies for supply quest!/Not much at the moment.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0014
  3: 0x0011 [0x01] GOTO 0x0014

SUBROUTINE_0014:
  4: 0x0014 [0x03] Work_Zone[1] = Work_Zone[0]
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```
