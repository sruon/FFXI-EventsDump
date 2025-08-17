# 17523228 - SUNACHI_TEST1

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Walk of Echoes (ID: 182) |
| Block Size       | 80 bytes                 |
| Total Events     | 2                        |
| References Count | 3                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [111](#event-111)     | 0x0001       |     43 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x1E0C      |        7692 |
|       2 | 0x0001      |           1 |

## String References

- **7692**: Occupy the hollow? [Yep./Nope.]

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

### Event 111

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 01 10 00 80 24 01  80 02 80 00 80 25 02 00   .....$......%..
0010: 10 00 80 00 1F 00 A7 00  A7 01 01 10 01 2A 00 02  .............*..
0020: 00 10 02 80 00 2A 00 01  2A 00 21 00              .....*..*.!.    
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[1] = 0*
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=7692*, default_option=1*, option_flags=0*)
    → "Occupy the hollow? [Yep./Nope.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001F
  4: 0x0016 [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response (Dynamis/MMM/Salvage), mode=0x00
  5: 0x0018 [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response with parameter (Dynamis/MMM/Salvage), param=Work_Zone[1]
  6: 0x001C [0x01] GOTO 0x002A
  7: 0x001F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002A
  8: 0x0027 [0x01] GOTO 0x002A

SUBROUTINE_002A:
  9: 0x002A [0x21] END_EVENT
 10: 0x002B [0x00] END_REQSTACK()
```
